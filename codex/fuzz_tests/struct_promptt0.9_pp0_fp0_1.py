import _struct
# Test _struct.Struct
from collections import namedtuple
from struct import unpack_from
from multidict._struct import Struct
from multidict._compat import BytesIO, PYPY
import pytest


class _StructMissingAttribute(object):
    def __init__(self, name):
        self.name = name

    def __getattr__(self, name):
        if name == self.name:
            raise AttributeError()
        else:
            raise RuntimeError('API changed')

    def __repr__(self):
        return '_StructMissingAttribute(name=%r)' % self.name


class _FakeRaw(object):
    def __init__(self, bigger_than_three):
        self.struct = _StructMissingAttribute(
            'pack_into' if bigger_than_three else 'pack')


class StructTests(object):

    def test_get_format_str(self):
        assert self.Struct.get_format_str() == self.format_str

    def test_unpack(self):
        data = _struct.pack(self.format
