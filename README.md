# betz-poetry-sample

Basic python packaging with `poetry` and using `argparse` to call different python scripts in a 
single package/cli. 

## Pre requisites 

**Install poetry into the global packges and allow it to create venvs in projects**

```shell
pip install poetry
poetry config virtualenvs.in-project true
```

## Installing the package dependencies using poetry 

Most of the time if you want to develop the package, you will need to install its dependencies.
You might be familiar with a `requirements.txt` in vanilla python, poetry uses `pyproject.toml`
to manage dependencies, program entry points and basically all config for the package. 

```shell
poetry install
```

## Building a wheel

The basic shippable unit of a python package, when you do a `pip install ...` you are installing _wheels_ under
the hood.  

```shell
poetry build
```

Now you will have a `dist` folder with your `*.whl` file in there.  This is the project with all the needful dependencies in there as well.

## Installing a wheel to a python venv (or the global packages)

```shell
pip install dist/betz_poetry_sample-1.0.0-py3-none-any.whl --force-reinstall
```

n.b. if you are working in a venv and just run `poetry install` you will have the `utils-cli` available without
having to build a _wheel_ or install it via pip. 

## Running the CLI

Get the help message
```shell 
utils-cli -h
```

SHA256 Hash the `README.md` file
```shell
utils-cli hash -f README.md
```

Or... do a `MD5` hash on the `README.md`
```shell
utils-cli hash -f README.md -a md5
```

Printing the shape of a table (col & row counts) 
```shell
utils-cli pandas print -f test.csv
```

Or... Print the table as well in `verbose` mode
```shell
utils-cli pandas print -f test.csv -v
```

You can also call `-h` (`--help`) at any level, `argparse` creates the argument help for you.
```shell
utils-cli hash -h
utils-cli pandas -h
utils-cli pandas print -h
```

## Useful links (docs)

* [Poetry](https://python-poetry.org/docs/)
* [argparse](https://docs.python.org/3/library/argparse.html)
