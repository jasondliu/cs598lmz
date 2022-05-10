import gc, weakref
from .utils import find, strip_\x00

class Doc(object):
    def __init__(self, name, build_functions=True, build_classes=True,
                 build_methods=True, build_exceptions=True, build_modules=True):
        self.name = name
        self.build_functions = build_functions
        self.build_classes = build_classes
        self.build_methods = build_methods
        self.build_exceptions = build_exceptions
        self.build_modules = build_modules
        self.modules = []
        self.functions = []
        self.classes = []
        self.methods = []
        self.exceptions = []
        self.build()

    def build(self):
        #print 'building doc for module:', self.name
        self.module = __import__(self.name, globals(), locals(), [], -1)
        module_name = self.module.__name__
        module_path = self.module.__file__
        module_version = self
