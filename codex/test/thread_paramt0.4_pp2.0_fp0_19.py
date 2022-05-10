import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n')).start()

#
#
#

from collections import deque

from . import core
from . import util

from .core import *
from .util import *

#
#
#

def _parse_args(args, kwargs, *names):
    """
    Parse the given args and kwargs into a dictionary of named arguments.

    :param args: The positional arguments to parse.
    :param kwargs: The keyword arguments to parse.
    :param names: The names of the arguments to parse.
    :return: A dictionary of named arguments.
    """
    if len(args) > len(names):
        raise TypeError('too many positional arguments')

    result = {}
    for name, value in zip(names, args):
        result[name] = value

    for name in names[len(args):]:
        value = kwargs.pop(name, None)
        if value is not None:
            result[name] = value

