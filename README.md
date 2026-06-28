# RepoSentinel

Offline Git safety gate for developers.

RepoSentinel blocks commit disasters before they reach GitHub:

- leaked .env files
- private keys
- GitHub/OpenAI-style tokens
- .venv
- node_modules
- .next
- dist
- build
- cache folders
- oversized accidental commits

## Install

python3 -m pip install .

## Use

reposentinel scan
reposentinel explain
reposentinel install-hook

Built by SYRA Labs.
