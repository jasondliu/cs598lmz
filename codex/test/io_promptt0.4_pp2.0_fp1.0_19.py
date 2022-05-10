import io
# Test io.RawIOBase
#
# This test checks that io.RawIOBase works as expected.
#
# Written by Antoine Pitrou <solipsis@pitrou.net>
# Ported to Python 3 by Petr Viktorin <encukou@gmail.com>

import io
import os
import sys
import unittest
import pickle
import struct
import tempfile
import weakref
import random
import contextlib

