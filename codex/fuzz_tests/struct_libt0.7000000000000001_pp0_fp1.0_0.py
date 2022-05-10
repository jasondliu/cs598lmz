import _struct
from _struct import Struct

from . import util

from .util import _bytes, _str, _int, _float, _decoded

from io import BytesIO as _BytesIO
from collections import namedtuple as _namedtuple

from pla.interfaces import *
from pla.image import *


class _metaclass(type):
    __structs = {}
    __dict__ = {}

    def __new__(cls, name, bases, dict):
        new = type.__new__(cls, name, bases, dict)

        if new is cla:
            return new

        for key, value in dict.items():
            if not isinstance(value, Struct):
                continue
            _metaclass.__dict__.setdefault(name, {})[key] = value

        return new

    def __getattr__(cls, name):
        return _metaclass.__dict__.get(cls.__name__, {}).get(name)

    @classmethod
    def __getitem__(cls, name):
