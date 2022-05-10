from types import FunctionType
list(FunctionType())
# TypeError: list() takes at most 1 argument (0 given)
list(FunctionType)[:][:]()
# TypeError: 'NoneType' object has no attribute '__getitem__'
list(FunctionType)[:][:](:)
# SyntaxError: invalid syntax
list(FunctionType)[:][:(:)]
# SyntaxError: invalid syntax
list(FunctionType)[:][:][:]
# TypeError: 'NoneType' object has no attribute '__getitem__'
list(FunctionType)[:][:](i for i in list(FunctionType)[:][:][:])
# TypeError: 'NoneType' object is not iterable
list(FunctionType)[:][:]((i for i in list(FunctionType)[:][:][:]))
# TypeError: 'NoneType' object is not iterable
list(FunctionType)[:][:]((i for i in list(FunctionType)[:][:][:])[:])
# TypeError: 'NoneType' object is not iterable
list(FunctionType)[:][:](range(1))
# TypeError:
