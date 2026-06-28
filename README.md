# RepoSentinel

![Python](https://img.shields.io/badge/python-3.9%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![CI](https://github.com/dougsanreis/reposentinel/actions/workflows/ci.yml/badge.svg)

> Offline Git safety gate that prevents secrets, build artifacts and unsafe commits before they reach GitHub.

RepoSentinel helps developers keep repositories clean and safe before mistakes become permanent.

## Why

Developers accidentally commit `.env`, private keys, tokens, `.venv`, `node_modules`, build outputs and oversized changes.

RepoSentinel blocks these problems locally before they reach GitHub.

## Install

See [docs/INSTALL.md](docs/INSTALL.md).

## Use

```bash
reposentinel explain
reposentinel scan
reposentinel install-hook
```

## Security

RepoSentinel runs locally. No telemetry. No cloud upload. No private SYRA dependency.

## Roadmap

See [ROADMAP.md](ROADMAP.md).

## License

MIT

Built by SYRA Labs.
