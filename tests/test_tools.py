# -*- coding: utf-8 -

"""Test the created constraints against approved constraints.

This file is part of project oemof (github.com/oemof/oemof). It's copyrighted
by the contributors recorded in the version control history of the file,
available from its original location oemof/tests/tool_tests.py

SPDX-License-Identifier: MIT
"""

import logging
import os
import warnings

import pytest
from oemof.tools import debugging
from oemof.tools import economics
from oemof.tools.logger import define_logging
from oemof.tools.logger import extend_basic_path
from oemof.tools.logger import get_basic_path


def test_helpers():
    get_basic_path()
    assert os.path.isdir(os.path.join(os.path.expanduser('~'), '.oemof'))
    new_dir = extend_basic_path('test_xf67456_dir')
    assert os.path.isdir(new_dir)
    get_basic_path()  # get basic path should not overwrite path
    assert os.path.isdir(new_dir)
    os.rmdir(new_dir)
    assert not os.path.isdir(new_dir)




def test_logger():
    filepath = define_logging()
    assert isinstance(filepath, str)
    assert filepath[-9:] == 'oemof.log'
    assert os.path.isfile(filepath)


def test_annuity():
    """Test annuity function of economics tool."""
    assert round(economics.annuity(1000, 10, 0.1)) == 163
    assert round(economics.annuity(capex=1000, wacc=0.1, n=10, u=5)) == 264
    assert round(economics.annuity(1000, 10, 0.1, u=5, cost_decrease=0.1)
                 ) == 222


def test_annuity_exceptions():
    """Test out-of-bounds-error of the annuity tool."""
    pytest.raises(ValueError, economics.annuity, 1000, 10, 2)
    pytest.raises(ValueError, economics.annuity, 1000, 0.5, 1)
    pytest.raises(
        ValueError, economics.annuity, 1000, 10, 0.1, u=0.3)
    pytest.raises(
        ValueError, economics.annuity, 1000, 10, 0.1, cost_decrease=-1)


def test_suspicious_usage_warning():
    msg = "My message."
    with warnings.catch_warnings(record=True) as w:
        warnings.warn(msg, debugging.SuspiciousUsageWarning)
        assert len(w) == 1
        assert msg, str(w[-1].message)
