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
from xml.parsers.xmlparser importIncrementalParser
from xml.parsers.xmlparser import Error
from xml.parsers.xmlparser import XML_PARAM_ENTITY_PARSING_NEVER
from xml.parsers.xmlparser import XML_PARAM_ENTITY_PARSING_UNLESS_STANDALONE
from xml.parsers.xmlparser import XML_PARAM_ENTITY_PARSING_ALWAYS
from xml.parsers.xmlparser import XML_PARAM_ENTITY_PARSING_UNKNOWN
TEST_INPUT1 = b
