import lzma
lzma.LZMAFile

import sys
import os
import re
import shutil
import subprocess
import tempfile
import time
import zipfile

import six

import pytest

from . import util
from .util import (
    assert_raises_regex,
    assert_raises_regex_raw,
    assert_raises_os_error,
    assert_raises_not_implemented_error,
    assert_raises_windows_error,
    assert_raises_unix_error,
    assert_raises_unix_error_raw,
    assert_raises_unix_error_nosys,
    assert_raises_unix_error_nosys_raw,
    assert_raises_unix_error_nosys_nosys,
    assert_raises_unix_error_nosys_nosys_raw,
    assert_raises_unix_error_nosys_nosys_nosys,
    assert_raises_unix_error_nosys_nosys_nosys_raw,
