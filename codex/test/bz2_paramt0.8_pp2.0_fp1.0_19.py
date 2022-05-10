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

