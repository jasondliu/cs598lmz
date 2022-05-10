import types
types.ModuleType

###

import types
type(sys) == types.ModuleType

###

import types
type(sys) is types.ModuleType

###使用type来判断

print(type(sys))

###使用isinstance()

print(isinstance(sys, types.ModuleType))

###使用issubclass()

print(issubclass(type(sys), types.ModuleType))

###使用__class__属性

class Example:
    pass

Example.__class__

#可以看到Example的__class__属性指向的是type类：

Example.__class__ is type

#使用__class__只能用在类上，而type()可以用在类和实例上

e = Example()

