# -*- coding: utf-8 -

"""Test the created constraints against approved constraints.

This file is part of project oemof (github.com/oemof/oemof). It's copyrighted
by the contributors recorded in the version control history of the file,
available from its original location oemof/tests/tool_tests.py

SPDX-License-Identifier: MIT
"""

import os
import warnings

from nose.tools import assert_raises_regexp
from nose.tools import eq_
from nose.tools import ok_
from oemof.tools import debugging
from oemof.tools import economics
from oemof.tools.logger import define_logging
from oemof.tools.logger import extend_basic_path
from oemof.tools.logger import get_basic_path


def test_helpers():
    get_basic_path()
    ok_(os.path.isdir(os.path.join(os.path.expanduser('~'), '.oemof')))
    new_dir = extend_basic_path('test_xf67456_dir')
    ok_(os.path.isdir(new_dir))
    os.rmdir(new_dir)
    ok_(not os.path.isdir(new_dir))


def test_logger():
    filepath = define_logging()
    ok_(isinstance(filepath, str))
    ok_(filepath[-9:] == 'oemof.log')
    ok_(os.path.isfile(filepath))


def test_annuity():
    """Test annuity function of economics tool."""
    ok_(round(economics.annuity(1000, 10, 0.1)) == 163)
    ok_(round(economics.annuity(capex=1000, wacc=0.1, n=10, u=5)) == 264)
    ok_(round(economics.annuity(1000, 10, 0.1, u=5, cost_decrease=0.1)) == 222)


def test_annuity_exceptions():
    """Test out-of-bounds-error of the annuity tool."""
    msg = "Input arguments for 'annuity' out of bounds!"
    assert_raises_regexp(ValueError, msg, economics.annuity, 1000, 10, 2)
    assert_raises_regexp(ValueError, msg, economics.annuity, 1000, 0.5, 1)
    assert_raises_regexp(
        ValueError, msg, economics.annuity, 1000, 10, 0.1, u=0.3)
    assert_raises_regexp(
        ValueError, msg, economics.annuity, 1000, 10, 0.1, cost_decrease=-1)


def test_suspicious_usage_warning():
    msg = "My message."
    with warnings.catch_warnings(record=True) as w:
        warnings.warn(msg, debugging.SuspiciousUsageWarning)
        ok_(len(w) == 1)
        eq_(msg, str(w[-1].message))
