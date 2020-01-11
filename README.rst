.. contents:: **package_name**
   :backlinks: top
   :depth: 2


Python package template: TODO
============================================
- Click ``[Use this template]`` button to create a new repository
- Replace templates:
    - from ``package_name`` to your package name within the repository
    - authorized information at ``<package_name>/__version__.py``


********************************************************


Summary
============================================


Usage
============================================

:Sample Code:
    .. code-block:: python

        # Sample code

:Output:
    .. code-block::

        # Output


Installation
============================================
::

    pip install <package_name>


Dependencies
============================================
Python 3.5+


Development
============================================

Setup
--------------------------------------------
::

    $ make setup

Running tests
--------------------------------------------
::

    $ tox

Code formatting
--------------------------------------------
::

    $ make fmt

Linting
--------------------------------------------
::

    $ make check

Release a package to PyPI
--------------------------------------------
::

    $ make build
    $ make release

- Prerequisites for release:
    - PyPI account
    - GPG key
