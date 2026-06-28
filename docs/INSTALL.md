# Installation

## Local install

```bash
git clone https://github.com/dougsanreis/reposentinel.git
cd reposentinel
python3 -m venv .venv
source .venv/bin/activate
pip install -e .
```

## Validate

```bash
reposentinel explain
reposentinel scan
python -m unittest discover -s tests -v
```
