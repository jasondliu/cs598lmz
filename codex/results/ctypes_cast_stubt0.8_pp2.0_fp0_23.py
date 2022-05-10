import ctypes
ctypes.cast(id(obj), ctypes.py_object).value

##__main__.Derived

##MySuper is Base
print(Derived.__mro__)

##print('*'*33)
##print(Derived.__bases__)
##print('*'*33)
##import inspect
##
##print(inspect.getmro(Derived))
##print('*'*33)
##print(inspect.getclasstree([Derived]))
##print('*'*33)
##
##print(Derived.__bases__)


##print(isinstance(Derived, object))
##print(Derived.mro())
##print(type(Derived).__bases__)
