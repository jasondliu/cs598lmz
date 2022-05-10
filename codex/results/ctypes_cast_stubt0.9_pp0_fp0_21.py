import ctypes
ctypes.cast(p, data)

struct module {
    const char *name;
    PyObject *(*exec)(PyObject *, PyObject *, PyObject *);
};

_PyImport_ExecCodeModule(name, co);

import types
from types import ModuleType

def exec_module(self, locals):
    co = self.__code__
    exec(co, self.__dict__, locals)

mp = ModuleType('mymod')
mp.__code__ = types.CodeType(0, 0, 0, 64, '', (), (), (), '', 'filename', 1, b'')
mp.__dict__ = {}
mp.__exec__ = exec_module

mp.__exec__(globals())

import types
from types import ModuleType
import ctypes
import sys

def get_code_object(filename):
    file = ctypes.WinDLL(filename)
    code_object = file.get_code()
    return code_object

def exec_module(self, locals):
    co = self.__code__
    sys.modules
