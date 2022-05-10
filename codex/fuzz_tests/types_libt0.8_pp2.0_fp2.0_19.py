import types
types.MethodType(lambda self: None, None, MyTraitClass)
'''

MyTraitClass.foo = MethodType(lambda self: None, None, MyTraitClass)
