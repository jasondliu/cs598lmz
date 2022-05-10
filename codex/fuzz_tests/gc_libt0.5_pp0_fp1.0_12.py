import gc, weakref
from . import types, objects
from .utils import get_module_name
from . import utils, builtins, exceptions, consts
from . import _types, _objects

class Module(types.Object):
    def __init__(self, modname):
        self.modname = modname
        self.globals = {}
        self.globals['__name__'] = modname
        self.globals['__doc__'] = None
        self.globals['__file__'] = None
        self.globals['__dict__'] = self.globals
        self.globals['__package__'] = None
        self.globals['__loader__'] = None
        self.globals['__builtins__'] = builtins.builtin_module
        self.globals['__cached__'] = None
        self.globals['__spec__'] = None
        self.globals['__path__'] = None
        self.globals['__docformat__'] = None
        self.globals['
