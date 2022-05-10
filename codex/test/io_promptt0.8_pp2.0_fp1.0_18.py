import io
# Test io.RawIOBase implementations
import unittest
import tempfile
import os
import random
import io
import sys
from io import BytesIO, StringIO, BufferedIOBase
from _io import BufferedWriter, BufferedReader, BufferedRWPair, BufferedRandom
from _pyio import IncrementalNewlineDecoder, TextIOWrapper
import _testbuffer
