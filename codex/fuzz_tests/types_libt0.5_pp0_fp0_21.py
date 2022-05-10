import types
types.__name__ = 'types'
import re
re.__name__ = 're'


class _Module(object):
    def __init__(self, name, module):
        self.__name__ = name
        self.__module__ = module.__name__
        self.__dict__.update(module.__dict__)

    def __getattr__(self, name):
        try:
            return self.__dict__[name]
        except KeyError:
            raise AttributeError(name)

sys = _Module('sys', sys)
types = _Module('types', types)
re = _Module('re', re)


#
# This is a hack to get around a bug in Python 2.7.0.
#
# In Python 2.7.0, the "types" module is not available when
# running under mod_python.  This is a bug that is fixed in
# 2.7.1.  The following code is a hack to make it possible
# to run under 2.7.0.  The code is based on the fact that
# the "
