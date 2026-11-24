# my_backend

A Python 3.12 starter for 3R Session 1. This scaffold was generated with
Cookiecutter using the package layout shown in the
[guided exercise](https://github.com/drweihungpan-lab/3R-teaching/blob/main/materials/exercises/session-1.md).

Set up an isolated environment, install the package, and run the example and tests:

```bash
python3.12 -m venv .venv
source .venv/bin/activate
python -m pip install -e .
my-backend 2 3 5
python -m unittest discover -s tests -v
```

The example prints `10`. The package code lives in `src/my_backend/`,
and `setup.cfg` connects the `my-backend` command to the Python entry point.
