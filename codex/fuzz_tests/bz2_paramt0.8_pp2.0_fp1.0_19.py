from bz2 import BZ2Decompressor
BZ2Decompressor

from collections import defaultdict
from io import BytesIO, SEEK_END
from itertools import zip_longest
from os import remove, environ
from os.path import isdir, join, exists
from shutil import rmtree
from signal import signal, SIGINT, SIGTERM
from subprocess import Popen, check_output, PIPE
from sys import stderr, getsizeof
from tempfile import NamedTemporaryFile, mkdtemp
from typing import Callable

import pytest

from uncompyle6.semantics import PYTHON3, PYTHON_VERSION
from uncompyle6.parser import PythonParser, get_python_parser, get_python_parser_description
from uncompyle6.scanners import get_scanner
from uncompyle6.semantics import SourceToCode
from uncompyle6.show import AbstractWriter, SourceWriter
from uncompyle6.version import __version__

from uncompyle6.tests.scanner import get_scanner_test_dir
from uncompyle6.tests.helper import get_uncompyle_cache_dir, get
