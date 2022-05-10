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
import functools
import contextlib
import gc
import pickle
import shutil
import stat
import struct
import subprocess
import threading
import time
import warnings
import random
import socket
import select
import array
import collections
import abc
import textwrap
import re
import platform
import locale
import copy
import itertools
import collections.abc

from test import support
from test.support import (
    TESTFN, unlink, run_with_locale, check_warnings,
    check_no_resource_warning, import_module, bigmemtest,
    cpython_only, requires_resource, requires_IEEE_754,
    requires_zlib, requires_bz2, requires_lzma, requires_gzip,
    requires_ssl, requires_pytz, requires_linux_version,
    requires_mac_ver, requires_freebsd_version,
    requires_aix_version, requires_sun
