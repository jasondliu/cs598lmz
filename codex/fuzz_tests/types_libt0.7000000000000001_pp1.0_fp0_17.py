import types
types.MethodType(lambda self: 42, None)

# ---

# Python3.3 is required
if sys.version_info < (3, 3):
    raise ImportError("This module requires Python 3.3 or higher")

# ---

import importlib
importlib.import_module("pygments.styles")

# ---

from collections.abc import Iterable
isinstance((), Iterable)

# ---

import inspect

def foo():
  pass

inspect.signature(foo)

# ---

from xml.etree.ElementTree import *
from io import StringIO

tree = parse(StringIO("<a><b/></a>"))
tree.find("b")

# ---

from collections import OrderedDict

d = OrderedDict()
d[42] = "answer"
list(d.keys())

# ---

from io import TextIOWrapper
TextIOWrapper(sys.stdin.buffer, "utf-8")

# ---

# Try-except blocks have new syntax (f
