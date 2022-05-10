from types import FunctionType
list(FunctionType(lambda: None, globals(), 'lambda'))

# TODO: how to check this?
# def f():
#     pass
# list(f)

# TODO: how to check this?
# class C:
#     pass
# list(C())
