import codecs
codecs.register_error('skip', codecs.lookup_error('ignore'))


# Using futurize to avoid > 2.7 code
import io          as _io
import os          as _os
import platform    as _platform
import re          as _re
import subprocess  as _subprocess
import sys         as _sys
import traceback   as _traceback

try:
    from . _types import IPyCompatTypes
    __type_lookup = IPyCompatTypes
except:
    from ._types import IPyCompatTypes as __type_lookup

try:                                                                                                       # pragma no cover
    # python 2.7+
    import collections.abc as _collections_abc
except ImportError:                                                                                        # pragma no cover
    # python 2.6
    import collections as _collections_abc

try:                                                                                                       # pragma no cover
    # python >= 3.5
    from typing import *
except ImportError:                                                                                        # pragma no cover
    # older
    pass



_PY3 = _sys.
