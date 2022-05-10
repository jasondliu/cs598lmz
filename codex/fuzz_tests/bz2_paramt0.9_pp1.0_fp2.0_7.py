from bz2 import BZ2Decompressor
BZ2Decompressor()

########### Python 3.2 #############
from http.client import HTTPSConnection
HTTPSConnection()

########### Python 3.3 #############
from html import unescape
unescape('&#8220;&#8221;')

########### Python 3.4 #############
import walker
walker.Walker()
"""

from test_python import TestPython
from test_python import INLINE_SCRIPTS
from test_python import EXTRA_SCRIPTS
from test_python import DEFAULT_DEPS


DEPS = OrderedDict()
DEPS.update(DEFAULT_DEPS)

# path -> bool
# If a path is an archive we won't bother with it anymore
ARCHIVES = {}

# Deps for each class
CLASSPATH_DEPS = {}


def find_python_lib_path():
    for dirpath, _, filenames in os.walk(python_lib_path):
        for filename in sorted(filenames):
            name, ext = os.path.splitext(filename)
            if ext == '.py
