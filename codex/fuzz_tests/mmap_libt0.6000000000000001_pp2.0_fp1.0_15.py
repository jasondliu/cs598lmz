import mmap
import os
import platform
import shutil
import sys
import tempfile
import time

import pytest

import fsspec
from fsspec.implementations.memory import MemoryFileSystem
from fsspec.utils import tokenize
from fsspec.spec import AbstractFileSystem
from fsspec.registry import Registry
from fsspec._version import get_versions

DEFAULT_BLOCK_SIZE = 2 ** 20
DEFAULT_BLOCK_SIZE_BYTES = 2 ** 20
DEFAULT_BLOCK_SIZE_KB = DEFAULT_BLOCK_SIZE_BYTES // 1024
DEFAULT_BLOCK_SIZE_MB = DEFAULT_BLOCK_SIZE_KB // 1024

# Make default block size configurable via environment variable
if "FSS_DEFAULT_BLOCK_SIZE" in os.environ:
    DEFAULT_BLOCK_SIZE = os.environ["FSS_DEFAULT_BLOCK_SIZE"]
    DEFAULT_BLOCK_SIZE_BYTES = int(DEFAULT_BLOCK_SIZE)
    DEFAULT_BLOCK_SIZE_
