import ctypes
ctypes.cast(0, ctypes.py_object).value

# This is a workaround for a bug in PyPy, see
# https://bitbucket.org/pypy/pypy/issue/1883/ctypes-cast-segfaults-with-pypy-on-osx
# and https://foss.heptapod.net/pypy/pypy/-/issues/3143
#
# The bug is fixed in PyPy 7.3.1, so we can remove this workaround once we
# require that version.
try:
    ctypes.cast(0, ctypes.py_object).value
except ValueError:
    pass

import sys
import os
import subprocess
import shutil
import errno
import warnings
import tempfile
import contextlib
import platform
import re
import json
import hashlib
import zipfile
import tarfile
import stat
import glob
import functools
import io
import base64
import logging
import distutils.spawn
import distutils.version
from collections import namedtuple
from collections import OrderedDict

