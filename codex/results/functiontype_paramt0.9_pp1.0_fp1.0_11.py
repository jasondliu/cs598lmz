from types import FunctionType
list(FunctionType('', '', (('a', 'b'), ('c', 'd'))), FunctionType('', '', None), FunctionType('', '', ()))

# testing for class objects

class A: pass
a = A()
sorted(list(A), list(a))

# testing for type objects
type('f', (object,), {})

sorted(list(type), list(object), list(type('', (object,), {})), list(type('', (), {})))

# testing for None
list(None)
