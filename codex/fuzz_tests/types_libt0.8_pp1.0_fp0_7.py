import types
types.ModuleType('os.path')  # doctest: +ELLIPSIS

# In Python 3.2+, there is a PEP-381-compatible pathlib module in
# stdlib:
try:
    import pathlib
except ImportError:
    pathlib = None
else:
    Path = types.ModuleType("pathlib")
    import pathlib.path
    if not hasattr(pathlib.path, "Path"):
        Path.Path = type("Path", (), {"__class__": Path})
    else:
        Path.Path = pathlib.path.Path

# pylint: disable=unused-variable
# pylint: disable=redefined-outer-name
# pylint: disable=invalid-name
# pylint: disable=unused-import
# pylint: disable=unused-argument
# pylint: disable=redefined-outer-name
# pylint: disable=unused-import

import random
import sys
from functools import partial
from itertools import product
from textwrap import dedent
from types import
