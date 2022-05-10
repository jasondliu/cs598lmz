from types import FunctionType
list(FunctionType(id))              # [id]
list(FunctionType(id, (), globals()))        # [<function id at 0x...>]
list(FunctionType(id, (), {'id': id}))       # []

# class types
list(ClassType(''))     # [<type 'str'>]
list(ClassType(None))   # [NoneType]
list(ClassType([]))     # [<type 'list'>]
list(ClassType(1))      # [<type 'int'>]

# for TypeError
'''
class Foo:
    pass
list(Foo)
'''
class Foo(object):
    pass
list(Foo)
list(Foo())

# test __iter__
def igen(seq):
    return iter(xrange(seq)) if seq > 0 else iter([])
list(igen(0))    # []
list(igen(1))    # [0]
list(igen(-1))   # []
