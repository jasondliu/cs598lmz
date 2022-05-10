import gc, weakref
import sys
import os

from . import _pytest

import pytest

def pytest_addoption(parser):
    group = parser.getgroup("general")
    group.addoption('--gc',
               action="store",
               dest="gc",
               default="",
               metavar="name",
               choices=("enable", "disable", "debug"),
               help="perform garbage collection checks at end of test run.")
    group.addoption('--no-gc-stats',
               action="store_true",
               dest="nogcstats",
               default=False,
               help="do not print out gc statistics at the end of the test run.")
    group.addoption('--no-python-warnings',
               action="store_true",
               dest="nopywarnings",
               default=False,
               help="do not print out python warnings at the end of the test run.")
    group.addoption('--pythonwarnings',
               action="store",
               dest="pythonwarnings",
               default="default",
               metavar="mode
