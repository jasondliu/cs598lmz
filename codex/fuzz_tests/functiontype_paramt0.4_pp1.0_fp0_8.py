from types import FunctionType
list(FunctionType(f.__code__, globals(), 'foo'))

# Test that the __code__ attribute of a function is writable.
import sys
def f(): pass
def g(): pass
f.__code__ = g.__code__
f()

# Test that the __code__ attribute of a function is writable.
import sys
def f(): pass
def g(): pass
f.__code__ = g.__code__
f()

# Test that the __code__ attribute of a function is writable.
def f(): pass
def g(): pass
f.__code__ = g.__code__
f()

# Test that the __code__ attribute of a function is writable.
def f(): pass
def g(): pass
f.__code__ = g.__code__
f()

# Test that the __code__ attribute of a function is writable.
def f(): pass
def g(): pass
f.__code__ = g.__code__
f()

# Test that the __code__ attribute of a function is writable.
def f(): pass
def g():
