import ctypes
ctypes.cast(0, ctypes.py_object).value

#-------------------------------------------------------------------------------

class _TestWeakref(object):
    def __init__(self):
        self.__dict__['foo'] = 1
        self.__dict__['bar'] = 2
        self.__dict__['baz'] = 3
        self.__dict__['spam'] = 4
        self.__dict__['eggs'] = 5
        self.__dict__['ham'] = 6
        self.__dict__['foo2'] = 7
        self.__dict__['bar2'] = 8
        self.__dict__['baz2'] = 9
        self.__dict__['spam2'] = 10
        self.__dict__['eggs2'] = 11
        self.__dict__['ham2'] = 12
        self.__dict__['foo3'] = 13
        self.__dict__['bar3'] = 14
        self.__dict__['baz3'] = 15
        self.__dict__['spam3'] = 16
        self.__dict__['eggs3
