import types
# Test types.FunctionType
# Two functions in a module state the obvious.
def is_function(): return True
def is_not_function(): return False

print(type(is_function) == types.FunctionType)
print(type(is_not_function) == types.FunctionType)

print(is_function.__class__)
print(is_not_function.__class__)

# True, False
# True, False
# <class 'function'>
# <class 'function'>


import types
# Test types.BuiltinFunctionType
# (These functions are built into Python.)
import os

print(type(len) == types.BuiltinFunctionType)
print(type(os.getcwd) == types.BuiltinFunctionType)

# True
# True

# Another helper function
import types
def get_content_type(file_path):
    suffix = file_path.split(".")[-1].lower()

    for content_type, suf_list in MIME_TYPE_MAP.items():
        if suffix in suf_list:
            return content_type
