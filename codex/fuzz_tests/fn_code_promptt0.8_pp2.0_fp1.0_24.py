fn = lambda: None
# Test fn.__code__
fn.__code__
# Test fn.__code__.co_code
fn.__code__.co_code
# Test fn.__code__.co_varnames
fn.__code__.co_varnames
# Test fn.__code__.co_argcount
fn.__code__.co_argcount
# Test fn.__code__.co_consts
fn.__code__.co_consts
# Test fn.__code__.co_names
fn.__code__.co_names


# Test class variables
class Dummy:
    pass


# Test Dummy.__dict__
Dummy.__dict__
# Test Dummy.__mro__
Dummy.__mro__
# Test Dummy.__doc__
Dummy.__doc__
# Test Dummy.__class__
Dummy.__class__

import sys

# Test sys.modules
sys.modules
# Test sys.path
sys.path
# Test sys.argv
sys.argv
# Test sys.exit()
# Test sys.exit
