import gc, weakref
from itertools import chain
import sys
from time import time
from types import MethodType
from weakref import WeakKeyDictionary

from . import _compat
from . import _compat_collections as _collections
from . import _compat_itertools as _itertools
from . import _compat_itertools_imap as _itertools_imap
from . import _compat_itertools_izip as _itertools_izip
from . import _compat_itertools_ifilter as _itertools_ifilter
from . import _compat_itertools_imap as _itertools_imap
from . import _compat_itertools_ifilterfalse as _itertools_ifilterfalse
from . import _compat_itertools_izip_longest as _itertools_izip_longest
from . import _compat_itertools_combinations as _itertools_combinations
from . import _compat_itertools_combinations_with_replacement as _
