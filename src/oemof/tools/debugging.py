# -*- coding: utf-8 -*-

"""Module contains tools facilitating debugging

This file is part of project oemof (github.com/oemof/oemof). It's copyrighted
by the contributors recorded in the version control history of the file,
available from its original location oemof/oemof/tools/economics.py

SPDX-License-Identifier: MIT
"""


class SuspiciousUsageWarning(UserWarning):
    """
    Warn the user about potentially dangerous usage.

    Some ways of using `oemof` are not necessarily wrong but could lead to
    hard to find bugs if done accidentally instead of intentionally. We
    use these warnings, and you can do too ;), in your code to warn users about
    these cases. If you know what you are doing and these warnings point you to
    things you are doing intentionally, you can easily switch them off.

    Note
    ----
    TODO: Fix ref!
    See :ref:`oemof_tools_debugging_suspicioususagewarningsolph_label` for more
    information.

    Examples
    --------
    >>> import warnings
    >>> warnings.filterwarnings("ignore", category=SuspiciousUsageWarning)
    """


class ExperimentalFeatureWarning(UserWarning):
    """
    Warn the user about use of experimental features.

    New modules first go to "experimental" ti highlight their unmature state.
    Sometimes, functionality is added to existing code. We use this warning
    to warn users in these cases.
    """
