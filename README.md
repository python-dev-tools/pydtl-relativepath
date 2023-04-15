# pydtl-relativepath
pydtl-relativepath tool from pydtl community can be used to solve many issues that occurs with relative paths and imports from various modules in your complex framework.

![Tests](https://github.com/python-dev-tools/pydtl-relativepath/actions/workflows/tests.yml/badge.svg)

# Installation

Run `pip install pydtl-relativepath`

# Usage

## Relative to Absolute Path Conversions

Whenever specifying a relative path use `rel2abs()`

See an Example below

    from pydtl_relativepath import rel2abs as r2a
    readmepath = r2a("README.txt")
    print(open(readmepath, mode="r", encoding="utf-8").read())

This will convert relative path specified to an absolute path relative to current file's directory

Here, readmepath contains the absolute path for README.txt file
and it is compatible with os.PathLike objects.

> Note: More Documentation (TBA)

> Note: Incomplete version | Development is in progress
