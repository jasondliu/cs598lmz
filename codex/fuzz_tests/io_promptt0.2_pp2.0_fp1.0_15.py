import io
# Test io.RawIOBase

import _io
import unittest
import weakref
import os
import sys
import io
import errno
import tempfile
import warnings
import functools
import contextlib
import pickle
import gc
import struct
import random
import subprocess
import select
import time
import socket
import threading
import platform
import locale
import collections
import array
import stat
import mmap

from test import support
from test.support import (
    TESTFN, run_with_locale, check_warnings, bigmemtest,
    unlink, cpython_only, requires_resource, requires_IEEE_754,
    requires_zlib, requires_bz2, requires_lzma, requires_gzip,
    requires_ssl, requires_pytz, requires_linux_version,
    requires_mac_ver, requires_freebsd_version, requires_aix_version,
    requires_sunos_version, requires_unicode,
    findfile, import_module,
    )

# TESTFN is encoded using the filesystem encoding, but we need a byte
