# -*- coding: utf-8

"""Helpers to log your modeling process with oemof.

This file is part of project oemof (github.com/oemof/oemof). It's copyrighted
by the contributors recorded in the version control history of the file,
available from its original location oemof/oemof/tools/logger.py

SPDX-License-Identifier: MIT
"""

import os
import sys
from logging import DEBUG
from logging import INFO
from logging import Formatter
from logging import StreamHandler
from logging import debug
from logging import getLogger
from logging import handlers
from logging import info


def define_logging(logpath=None, logfile='oemof.log', file_format=None,
                   screen_format=None, file_datefmt=None, screen_datefmt=None,
                   screen_level=INFO, file_level=DEBUG, log_path=True,
                   timed_rotating=None):

    r"""Initialise customisable logger.

    Parameters
    ----------
    logfile : str
        Name of the log file, default: oemof.log
    logpath : str
        The path for log files. By default a ".oemof' folder is created in your
        home directory with subfolder called 'log_files'.
    file_format : str
        Format of the file output.
        Default: "%(asctime)s - %(levelname)s - %(module)s - %(message)s"
    screen_format : str
        Format of the screen output.
        Default: "%(asctime)s-%(levelname)s-%(message)s"
    file_datefmt : str
        Format of the datetime in the file output. Default: None
    screen_datefmt : str
        Format of the datetime in the screen output. Default: "%H:%M:%S"
    screen_level : int
        Level of logging to stdout. Default: 20 (logging.INFO)
    file_level : int
        Level of logging to file. Default: 10 (logging.DEBUG)
    log_path : boolean
        If True the used file path is logged while initialising the logger.
    timed_rotating : dict
        Option to pass parameters to the TimedRotatingFileHandler.


    Returns
    -------
    str : Place where the log file is stored.

    Notes
    -----
    By default the INFO level is printed on the screen and the DEBUG level
    in a file, but you can easily configure the logger.
    Every module that wants to create logging messages has to import the
    logging module. The oemof logger module has to be imported once to
    initialise it.

    Examples
    --------
    To define the default logger you have to import the python logging
    library and this function. The first logging message should be the
    path where the log file is saved to.

    >>> import logging
    >>> from oemof.tools import logger
    >>> mypath = logger.define_logging(
    ...     log_path=True, timed_rotating={'backupCount': 4},
    ...     screen_level=logging.ERROR, screen_datefmt = "no_date")
    >>> mypath[-9:]
    'oemof.log'
    >>> logging.debug("Hallo")
    """

    if logpath is None:
        logpath = extend_basic_path('log_files')

    file = os.path.join(logpath, logfile)

    log = getLogger('')

    # Remove existing handlers to avoid interference.
    log.handlers = []
    log.setLevel(DEBUG)

    if file_format is None:
        file_format = (
            "%(asctime)s - %(levelname)s - %(module)s - %(message)s")
    file_formatter = Formatter(file_format, file_datefmt)

    if screen_format is None:
        screen_format = "%(asctime)s-%(levelname)s-%(message)s"
    if screen_datefmt is None:
        screen_datefmt = "%H:%M:%S"
    screen_formatter = Formatter(screen_format, screen_datefmt)

    tmp_formatter = Formatter("%(message)s")

    ch = StreamHandler(sys.stdout)
    ch.setFormatter(screen_formatter)
    ch.setLevel(screen_level)
    log.addHandler(ch)

    timed_rotating_p = {
        'when': 'midnight',
        'backupCount': 10}

    if timed_rotating is not None:
        timed_rotating_p.update(timed_rotating)

    fh = handlers.TimedRotatingFileHandler(file, **timed_rotating_p)
    fh.setFormatter(tmp_formatter)
    fh.setLevel(file_level)
    log.addHandler(fh)

    debug("******************************************************")
    fh.setFormatter(file_formatter)
    if log_path:
        info("Path for logging: {0}".format(file))
    return file


def extend_basic_path(subfolder):
    """Returns a path based on the basic oemof path and creates it if
     necessary. The subfolder is the name of the path extension.
    """
    extended_path = os.path.join(get_basic_path(), subfolder)
    if not os.path.isdir(extended_path):
        os.mkdir(extended_path)
    return extended_path


def get_basic_path():
    """Returns the basic oemof path and creates it if necessary.
    The basic path is the '.oemof' folder in the $HOME directory.
    """
    basicpath = os.path.join(os.path.expanduser('~'), '.oemof')
    if not os.path.isdir(basicpath):
        os.mkdir(basicpath)
    return basicpath
