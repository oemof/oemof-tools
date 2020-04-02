========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |travis| |appveyor| |requires|
        | |coveralls| |codecov|
        | |scrutinizer| |codacy| |codeclimate|
    * - package
      - | |version| |wheel| |supported-versions| |supported-implementations|
        | |commits-since|
.. |docs| image:: https://readthedocs.org/projects/oemof-tools/badge/?style=flat
    :target: https://readthedocs.org/projects/oemof-tools
    :alt: Documentation Status

.. |travis| image:: https://api.travis-ci.org/oemof/oemof-tools.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/oemof/oemof-tools

.. |appveyor| image:: https://ci.appveyor.com/api/projects/status/github/oemof/oemof-tools?branch=master&svg=true
    :alt: AppVeyor Build Status
    :target: https://ci.appveyor.com/project/oemof/oemof-tools

.. |requires| image:: https://requires.io/github/oemof/oemof-tools/requirements.svg?branch=master
    :alt: Requirements Status
    :target: https://requires.io/github/oemof/oemof-tools/requirements/?branch=master

.. |coveralls| image:: https://coveralls.io/repos/oemof/oemof-tools/badge.svg?branch=master&service=github
    :alt: Coverage Status
    :target: https://coveralls.io/r/oemof/oemof-tools

.. |codecov| image:: https://codecov.io/gh/oemof/oemof-tools/branch/master/graphs/badge.svg?branch=master
    :alt: Coverage Status
    :target: https://codecov.io/github/oemof/oemof-tools

.. |codacy| image:: https://img.shields.io/codacy/grade/CODACYTOKEN.svg
    :target: https://www.codacy.com/app/oemof/oemof-tools
    :alt: Codacy Code Quality Status

.. |codeclimate| image:: https://codeclimate.com/github/oemof/oemof-tools/badges/gpa.svg
   :target: https://codeclimate.com/github/oemof/oemof-tools
   :alt: CodeClimate Quality Status

.. |version| image:: https://img.shields.io/pypi/v/oemof-tools.svg
    :alt: PyPI Package latest release
    :target: https://pypi.org/project/oemof-tools

.. |wheel| image:: https://img.shields.io/pypi/wheel/oemof-tools.svg
    :alt: PyPI Wheel
    :target: https://pypi.org/project/oemof-tools

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/oemof-tools.svg
    :alt: Supported versions
    :target: https://pypi.org/project/oemof-tools

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/oemof-tools.svg
    :alt: Supported implementations
    :target: https://pypi.org/project/oemof-tools

.. |commits-since| image:: https://img.shields.io/github/commits-since/oemof/oemof-tools/v0.4.0.dev0.svg
    :alt: Commits since latest release
    :target: https://github.com/oemof/oemof-tools/compare/v0.4.0.dev0...master


.. |scrutinizer| image:: https://img.shields.io/scrutinizer/quality/g/oemof/oemof-tools/master.svg
    :alt: Scrutinizer Status
    :target: https://scrutinizer-ci.com/g/oemof/oemof-tools/


.. end-badges

Tiny tools of the oemof project.

* Free software: MIT license

Installation
============

::

    pip install oemof-tools

You can also install the in-development version with::

    pip install https://github.com/oemof/oemof-tools/archive/master.zip


Documentation
=============


https://oemof-tools.readthedocs.io/


Development
===========

To run the all tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox

