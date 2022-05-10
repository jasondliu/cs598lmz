import weakref

from . import _core
from . import _util
from . import _compat
from . import _errors
from . import _types
from . import _constants
from . import _lib
from . import _version

from . import _lazy_import
_lazy_import.lazy_import(globals(), """
import collections.abc
import contextlib
import datetime
import decimal
import functools
import itertools
import operator
import os
import re
import sys
import threading
import time
import traceback

from collections import namedtuple

from . import _ext
from . import _json
from . import _protocol
from . import _types
from . import _util
from . import _version

from . import _lazy_import
""")

