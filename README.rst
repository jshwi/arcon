arcon
=====
.. image:: https://img.shields.io/badge/License-MIT-yellow.svg
    :target: https://opensource.org/licenses/MIT
    :alt: License
.. image:: https://img.shields.io/pypi/v/arcon
    :target: https://img.shields.io/pypi/v/arcon
    :alt: pypi
.. image:: https://github.com/jshwi/arcon/actions/workflows/ci.yml/badge.svg
    :target: https://github.com/jshwi/arcon/actions/workflows/ci.yml
    :alt: CI
.. image:: https://github.com/jshwi/arcon/actions/workflows/codeql-analysis.yml/badge.svg
    :target: https://github.com/jshwi/arcon/actions/workflows/codeql-analysis.yml
    :alt: CodeQL
.. image:: https://codecov.io/gh/jshwi/arcon/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/jshwi/arcon
    :alt: codecov.io
.. image:: https://readthedocs.org/projects/arcon/badge/?version=latest
    :target: https://arcon.readthedocs.io/en/latest/?badge=latest
    :alt: readthedocs.org
.. image:: https://img.shields.io/badge/python-3.8-blue.svg
    :target: https://www.python.org/downloads/release/python-380
    :alt: python3.8
.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://github.com/psf/black
    :alt: black

Persistent runtime config
-------------------------

Child class of ``argparse.ArgumentParser``

Includes version argument as a default

Default values are defined through pyproject.toml

Includes additional argument adding methods

.. code-block:: python

    >>> __version__ = "0.1.0"
    >>> from arcon import ArgumentParser

Parsing comma separated list

.. code-block:: python

    >>> parser = ArgumentParser(__version__)
    >>> parser.add_list_argument("-l", "--list")
    >>> parser.parse_args(["--list", "comma,separated,list"])
    Namespace(list=['comma', 'separated', 'list'])

Parsing dict of comma separated lists

.. code-block:: python

    >>> parser = ArgumentParser(__version__)
    >>> parser.add_dict_argument("-d", "--dict")
    >>> parser.parse_args(["--dict", "key=comma,separated,list"])
    Namespace(dict={'key': ['comma', 'separated', 'list']})
