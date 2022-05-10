import codecs
# Test codecs.register_error
import os
import pickle
import random
import re
import shutil
import stat
import string
import subprocess
import sys
import tempfile
import textwrap
import time
import unittest
from test import support
from test.support import TESTFN, run_unittest, unlink, import_module, \
    cpython_only, check_warnings, check_impl_detail, requires_zlib, \
    requires_bz2, requires_lzma, requires_gzip, requires_xz, \
    bigmemtest, bigaddrspacetest, _2G, _4G, _4G, _4G, _4G, _4G, _4G, \
    _4G, _4G, _4G, _4G, _4G, _4G, _4G, _4G, _4G, _4G, _4G, _4G, _4G, \
    _4G, _4G, _4G, _4G, _4G, _4G, _4G, _4G, _4
