Status: Archived
==================
This repository has been archived and is no longer maintained

arcon
=====
|Archive| |License| |PyPI| |CI| |CodeQL| |pre-commit.ci status| |codecov.io| |readthedocs.org| |python3.8| |Black| |isort| |docformatter| |pylint| |Security Status| |Known Vulnerabilities| |arcon|

.. |Archive| image:: https://img.shields.io/badge/status-inactive-red.svg
    :target: https://img.shields.io/badge/status-inactive-red.svg
    :alt: Status Inactive
.. |License| image:: https://img.shields.io/badge/License-MIT-yellow.svg
    :target: https://opensource.org/licenses/MIT
    :alt: License
.. |PyPI| image:: https://img.shields.io/pypi/v/arcon
    :target: https://pypi.org/project/arcon/
    :alt: PyPI
.. |CI| image:: https://github.com/jshwi/arcon/actions/workflows/build.yaml/badge.svg
    :target: https://github.com/jshwi/arcon/actions/workflows/build.yaml
    :alt: Build
.. |CodeQL| image:: https://github.com/jshwi/arcon/actions/workflows/codeql-analysis.yml/badge.svg
    :target: https://github.com/jshwi/arcon/actions/workflows/codeql-analysis.yml
    :alt: CodeQL
.. |pre-commit.ci status| image:: https://results.pre-commit.ci/badge/github/jshwi/arcon/master.svg
   :target: https://results.pre-commit.ci/latest/github/jshwi/arcon/master
   :alt: pre-commit.ci status
.. |codecov.io| image:: https://codecov.io/gh/jshwi/arcon/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/jshwi/arcon
    :alt: codecov.io
.. |readthedocs.org| image:: https://readthedocs.org/projects/arcon/badge/?version=latest
    :target: https://arcon.readthedocs.io/en/latest/?badge=latest
    :alt: readthedocs.org
.. |python3.8| image:: https://img.shields.io/badge/python-3.8-blue.svg
    :target: https://www.python.org/downloads/release/python-380
    :alt: python3.8
.. |Black| image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://github.com/psf/black
    :alt: Black
.. |isort| image:: https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336
    :target: https://pycqa.github.io/isort/
    :alt: isort
.. |docformatter| image:: https://img.shields.io/badge/%20formatter-docformatter-fedcba.svg
    :target: https://github.com/PyCQA/docformatter
    :alt: docformatter
.. |pylint| image:: https://img.shields.io/badge/linting-pylint-yellowgreen
    :target: https://github.com/PyCQA/pylint
    :alt: pylint
.. |Security Status| image:: https://img.shields.io/badge/security-bandit-yellow.svg
    :target: https://github.com/PyCQA/bandit
    :alt: Security Status
.. |Known Vulnerabilities| image:: https://snyk.io/test/github/jshwi/arcon/badge.svg
    :target: https://snyk.io/test/github/jshwi/arcon/badge.svg
    :alt: Known Vulnerabilities
.. |arcon| image:: https://snyk.io/advisor/python/docsig/badge.svg
  :target: https://snyk.io/advisor/python/arcon
  :alt: arcon

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
