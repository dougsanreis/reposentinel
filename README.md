# RepoSentinel

> Offline Git safety gate that prevents secrets, build artifacts and unsafe commits before they reach GitHub.

RepoSentinel helps developers avoid common repository mistakes before they are committed or pushed.

## Install

```bash
python3 -m pip install .
```

## Use

```bash
reposentinel explain
reposentinel scan
reposentinel install-hook
```

## What it detects

- `.env` files
- private keys
- GitHub/OpenAI-style tokens
- `.venv`
- `node_modules`
- `.next`
- `dist`
- `build`
- cache folders
- oversized accidental commits

## Why it is different

- Offline first
- Zero telemetry
- Git-native
- Fast
- Simple
- Built for developer workflows

## Security

RepoSentinel runs locally and does not collect data.

## License

MIT

Built by SYRA Labs.
