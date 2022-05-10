import ctypes
ctypes.cast(0xf7421000, ctypes.py_object).value


import objc

ObjCClass = objc.lookUpClass('ObjCClass')
NSObject = objc.lookUpClass('NSObject')

class PyObjectBridge(NSObject):
    __slots__ = ('name', 'x', 'controller')

    def init(self):
        self = super(PyObjectBridge, self).init()
        if self is None:
            return None

        self.controller = ObjCClass.alloc().init()
        self.controller.retain()

        self.x = 42

        return self

    def setName_(self, value):
        self.name = value
        self.controller.setName_(self.name)

    def setX_(self, value):
        self.x = value
        self.controller.setX_(self.x)

    def x(self):
        return self.x

    def valueForKey_(self, key):
        return getattr(self, key)

    def setValue_forKey_(self, value, key):
        setattr
