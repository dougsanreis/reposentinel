from __future__ import annotations
import re
import subprocess
import sys
from pathlib import Path

BLOCKED_PATHS = {".env", ".venv", "venv", "node_modules", "dist", "build", ".next", ".cache", "__pycache__", "recovery_broken_archive"}
SECRET_PATTERNS = [r"ghp_[A-Za-z0-9_]{20,}", r"sk-[A-Za-z0-9]{20,}", r"-----BEGIN (RSA |OPENSSH |EC )?PRIVATE KEY-----"]

def staged_files() -> list[str]:
    r = subprocess.run(["git", "diff", "--cached", "--name-only"], text=True, capture_output=True, check=False)
    return [x.strip() for x in r.stdout.splitlines() if x.strip()]

def has_blocked_path(path: str) -> bool:
    parts = set(path.replace("\\", "/").split("/"))
    return bool(parts & BLOCKED_PATHS)

def scan() -> int:
    violations = []
    files = staged_files()
    for file in files:
        if has_blocked_path(file):
            violations.append(("BLOCKED_PATH", file))
        p = Path(file)
        if p.exists() and p.is_file():
            text = p.read_text(errors="ignore")
            for pattern in SECRET_PATTERNS:
                if re.search(pattern, text):
                    violations.append(("POSSIBLE_SECRET", file))
    if len(files) > 30:
        violations.append(("TOO_MANY_STAGED_FILES", str(len(files))))
    if violations:
        print("RepoSentinel blocked this commit:")
        for kind, target in violations:
            print(f"- {kind}: {target}")
        return 1
    print("RepoSentinel: repository gate passed.")
    return 0

def explain() -> int:
    print("RepoSentinel prevents leaked secrets, dependency folders, build artifacts and oversized accidental commits before they reach GitHub.")
    return 0

def install_hook() -> int:
    hook = Path(".git/hooks/pre-commit")
    hook.parent.mkdir(parents=True, exist_ok=True)
    hook.write_text("#!/usr/bin/env bash\nreposentinel scan\n")
    hook.chmod(0o755)
    print("RepoSentinel pre-commit hook installed.")
    return 0

def main() -> int:
    cmd = sys.argv[1] if len(sys.argv) > 1 else "scan"
    return scan() if cmd == "scan" else explain() if cmd == "explain" else install_hook() if cmd == "install-hook" else 2

if __name__ == "__main__":
    raise SystemExit(main())
