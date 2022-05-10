import lzma
# Test LZMADecompressor.

import unittest
import io
import os
import struct
import sys
import tempfile
import time
import warnings
import zlib

from test import support
