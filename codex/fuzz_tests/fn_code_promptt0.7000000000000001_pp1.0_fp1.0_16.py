fn = lambda: None
# Test fn.__code__.co_filename

import os
import types

print(types.FunctionType.__code__.co_filename)

def f(): pass
f.__code__.co_filename = 'test'
print(f.__code__.co_filename)
f.__code__.co_filename = 5
f.__code__.co_filename += 'a'
print(f.__code__.co_filename)

try:
    f.__code__.co_filename = type
except TypeError:
    print("TypeError")

try:
    f.__code__.co_filename = object
except TypeError:
    print("TypeError")

try:
    f.__code__.co_filename = complex
except TypeError:
    print("TypeError")

try:
    f.__code__.co_filename = None
except TypeError:
    print("TypeError")

try:
    f.__code__.co_filename = f
except TypeError:
    print("TypeError")

try:
    f.__code
