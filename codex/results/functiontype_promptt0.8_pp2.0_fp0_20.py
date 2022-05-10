import types
# Test types.FunctionType, but don't actually call it --
# the real test of that is test_callableobjects.py
x = types.FunctionType
del x
