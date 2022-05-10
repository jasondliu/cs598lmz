import gc, weakref
import sys

from . import _pytest

def pytest_addoption(parser):
    group = parser.getgroup("general")
    group.addoption('--gc-option', action="append",
        dest="gc_options", metavar="NAME=VALUE", default = [],
        help="Set an option to be used during garbage collection.")
    group.addoption('--gc-threshold', action="store",
        dest="gc_threshold", metavar="THRESHOLD", default = None,
        help="Set the garbage collection threshold (the number of unreachable objects after which garbage collection starts).")
    group.addoption('--gc-debug', action="store_true",
        dest="gc_debug", default=False,
        help="Enable debug output from the garbage collector.")

def pytest_configure(config):
    if config.option.gc_debug:
        gc.set_debug(gc.DEBUG_STATS)
    if config.option.gc_threshold is not None:
        try:
            gc.set_threshold(int
