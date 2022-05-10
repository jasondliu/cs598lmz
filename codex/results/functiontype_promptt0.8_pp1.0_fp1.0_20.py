import types
# Test types.FunctionType directly.
print('FunctionType:', types.FunctionType)
print('FunctionType:', types.FunctionType.__name__)
# Test types.CodeType directly.
print('CodeType:', types.CodeType)
print('CodeType:', types.CodeType.__name__)


# Notes:
# - Python versions prior to 2.6, 2.7, 3.1 all had a different CodeType type,
#   so if your code is meant to run on older versions, don't rely on types.CodeType
#   being a class, but instead just check for its name (== 'code').
# - Python versions prior to 2.7, 3.2 had a different FunctionType type,
#   so if your code is meant to run on older versions, don't rely on types.FunctionType
#   being a class, but instead just check for its name (== 'function').
# - Some other built-in functions may return objects of a different type
#   than types.FunctionType, so try to avoid using the type check for functions
#   when you can, and just use isinstance() instead.


