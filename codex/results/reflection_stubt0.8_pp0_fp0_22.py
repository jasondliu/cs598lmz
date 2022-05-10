fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

try:
    from collections import OrderedDict
except ImportError:
    from ordereddict import OrderedDict

import sys

try:
    from collections import UserList
except ImportError:
    from UserList import UserList

try:
    from collections import UserDict
except ImportError:
    from UserDict import UserDict

try:
    from collections import UserString
except ImportError:
    from UserString import UserString

attr_error = AttributeError if PY2 else TypeError
dunder_file = "__file__"
dunder_name = "__name__"
dunder_qualname = "__qualname__"
dunder_class = "__class__"
broken_kwargs = () if PY2 else ("__self__",)

__author__ = "Steven Loria, Alexander Schepanovski"
__version__ = "1.1.0"


def get_annotations(func):
    if hasattr(inspect, 'getfullargspec'):
        spec = inspect.getfull
