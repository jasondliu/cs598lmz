import types
types.ClassType
# <type 'classobj'>
#classobj is most probably an old style class
#from types import ClassType
#<type 'types.ClassType'>
#from types import *
#<type 'classobj'>


object()
# <object object at 0x7fcc5d6b3a40>
object.__class__
# <type 'type'>

import types
isinstance(object,types.TypeType)
#True

isinstance(object,ClassType)
#False

##Case 2
class MyClass():
    pass

type(MyClass)
# <type 'type'>

myobject = MyClass()
type(myobject)
#<class '__main__.MyClass'>

