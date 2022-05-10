import io
# Test io.RawIOBase.readinto()

import sys
from test import support
from io import BytesIO, SEEK_SET
from io import IOBase, BufferedIOBase, RawIOBase, BufferedReader, BufferedWriter
from io import BufferedRWPair
from io import TextIOWrapper, BufferedRandom

# Stub base classes

class MyRawIOBase(RawIOBase):
    def readinto(self, b):
        return 0

class MyBufferedReader(BufferedReader):
    def readinto(self, b):
        return 0

class MyBufferedWriter(BufferedWriter):
    def readinto(self, b):
        return 0

class MyBufferedRWPair(BufferedRWPair):
    def readinto(self, b):
        return 0

class MyBufferedRandom(BufferedRandom):
    def readinto(self, b):
        return 0

class MyTextIOWrapper(TextIOWrapper):
    def readinto(self, b):
        return 0


# Helper to check that a given IO object raises an
