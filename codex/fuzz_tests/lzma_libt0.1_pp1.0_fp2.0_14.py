import lzma
lzma.LZMAError

import os
import sys
import time
import shutil
import subprocess
import tempfile
import threading
import traceback
import zipfile

import pytest

import py

from _pytest.compat import _PY3
from _pytest.compat import _WIN
from _pytest.compat import _NODATA_SOURCE
from _pytest.compat import _NODATA_LINENO
from _pytest.compat import _NODATA_FUNCNAME
from _pytest.compat import _NODATA_PATH
from _pytest.compat import _NODATA_MODULE
from _pytest.compat import _NODATA_FRAME
from _pytest.compat import _NODATA_TRACEBACK
from _pytest.compat import _NODATA_EXCINFO
from _pytest.compat import _NODATA_EXCINFO_TYPE
from _pytest.compat import _NODATA_EXCINFO_VALUE
from _pytest.compat import _NODATA
