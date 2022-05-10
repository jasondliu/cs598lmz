import types
types.ModuleType.__dict__['__mro__'] = (object,)
types.ModuleType.__dict__['__getattr__'] = types.ModuleType.__dict__['__getattribute__']
import sys
sys.modules['__main__'].__dict__['__getattr__'] = sys.modules['__main__'].__dict__['__getattribute__']
sys.modules['__main__'].__dict__['__setattr__'] = sys.modules['__main__'].__dict__['__setattr__']
#sys.modules['__main__'].__dict__['__getattr__'] = lambda self, name: sys.modules['__main__'].__dict__['__getattribute__'](self, name)
#sys.modules['__main__'].__dict__['__setattr__'] = lambda self, name, value: sys.modules['__main__'].__dict__['__setattr__'](self, name, value)

#sys.modules['__main__'].__dict__['__getattr__'] = lambda self, name: sys
