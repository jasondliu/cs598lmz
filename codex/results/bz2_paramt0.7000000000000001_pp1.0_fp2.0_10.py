from bz2 import BZ2Decompressor
BZ2Decompressor.__module__ = "bz2"  # work around https://bugs.python.org/issue14154

from . import _pytest
from .main import EXIT_INTERRUPTED, EXIT_NOTESTSCOLLECTED, EXIT_NOTESTSFAILED, EXIT_OK, main
from .config import _prepareconfig


def pytest_addoption(parser):
    group = parser.getgroup("general")
    group.addoption(
        '--capture',
        action="store",
        dest="capture",
        default="fd",
        metavar="method",
        choices=['fd', 'sys', 'no'],
        help="method used to capture stdout/stderr",
    )
    group.addoption(
        "--exitfirst",
        action="store_true",
        default=False,
        help="exit instantly on first error or failed test.",
    )
    group.addoption(
        "--maxfail",
        type=int,
        default=0,
        metavar="num",
       
