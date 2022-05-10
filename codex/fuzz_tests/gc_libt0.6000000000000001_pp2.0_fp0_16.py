import gc, weakref, traceback

from . import _gdbmi
from . import _glibobj
from . import _glibobj_enum
from . import _glibobj_flags
from . import _glibobj_object
from . import _glibobj_struct
from . import _glibobj_boxed


class GType:
    _gtypes = weakref.WeakValueDictionary()

    def __new__(cls, name):
        if name in cls._gtypes:
            return cls._gtypes[name]
        else:
            obj = super().__new__(cls)
            obj.name = name
            cls._gtypes[name] = obj
            return obj

    def __repr__(self):
        return '<GType %r>' % self.name


class GValue:
    def __init__(self, type):
        self.type = type
        self.value = None


class GObject:
    def __init__(self, ptr):
        self.__ptr = ptr
        self.__weakref = weak
