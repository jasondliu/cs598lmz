fn = lambda: None
# Test fn.__code__.co_filename
import os
import os.path
fn.__code__.co_filename = os.path.abspath(fn.__code__.co_filename)
# Test fn.__code__.co_firstlineno
fn.__code__.co_firstlineno = fn.__code__.co_firstlineno - 1
# Test fn.__code__.co_flags
fn.__code__.co_flags = fn.__code__.co_flags - 1
# Test fn.__code__.co_lnotab
fn.__code__.co_lnotab = fn.__code__.co_lnotab + b'\x00\x01'
# Test fn.__code__.co_stacksize
fn.__code__.co_stacksize = fn.__code__.co_stacksize + 1
# Test fn.__code__.co_varnames
fn.__code__.co_varnames = fn.__code__.co_varnames + (1,)
# Test fn.__code__.co
