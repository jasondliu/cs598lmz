import gc, weakref

from . import __version__
from . import _pyflakes_imports
from . import pyflakes_checker
from . import pyflakes_visitor
from . import pyflakes_util
from . import pyflakes_report
import pyflakes_checker

from pyflakes_util import checkPath

from pyflakes_checker import Checker, Builtins

from pyflakes_report import (
    print_header, print_error, print_warning, print_message
)

def check(codeString, filename, reporter=None):
    """
    Check the Python source given by C{codeString} for flakes.

    @param codeString: The Python source to check.
    @type codeString: C{str}

    @param filename: The name of the file the source came from, used to report
        errors.
    @type filename: C{str}

    @param reporter: A L{pyflakes.reporter.Reporter} instance, where errors and
        warnings will be reported.
    @type reporter: L{pyflakes.reporter
