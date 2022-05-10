import gc, weakref

from . import _core

_core.init()

class _PythonObject(object):
    def __init__(self, obj):
        self._obj = weakref.ref(obj)

    def __call__(self, *args, **kwargs):
        return self._obj()(*args, **kwargs)

class _PythonProxy(object):
    def __init__(self, obj):
        self._obj = weakref.ref(obj)

    def __getattr__(self, name):
        return getattr(self._obj(), name)

class _PythonFunction(object):
    def __init__(self, func):
        self._func = weakref.ref(func)

    def __call__(self, *args, **kwargs):
        return self._func()(*args, **kwargs)

class _PythonType(object):
    def __init__(self, type):
        self._type = weakref.ref(type)

    def __call__(self, *args, **kwargs):
        return self._type()(*args
