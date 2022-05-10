import mmap
# Test mmap.mmap()
import os
from io import StringIO
from io import BytesIO
from os import SEEK_SET
from os import SEEK_CUR
from os import SEEK_END
from os import strerror
from tempfile import mkstemp
from test.support import TESTFN
from test.support import unlink
from test.support import import_module
pyexpat = import_module('pyexpat')
import unittest
from xml.parsers.xmlparser import DefualtConsumer
