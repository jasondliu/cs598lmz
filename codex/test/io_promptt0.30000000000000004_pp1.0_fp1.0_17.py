import io
# Test io.RawIOBase
#
# This test checks that io.RawIOBase works as expected.
#
# The tests are designed to be run with a variety of raw IO objects,
# including the builtin open(), and io.FileIO().  The tests are run
# both in text and binary mode.
#
# Written by Amaury Forgeot d'Arc and Antoine Pitrou

import unittest
import io
import os
import sys
import tempfile
import errno
import random
import struct
import shutil
import stat
import contextlib
import warnings
import weakref

