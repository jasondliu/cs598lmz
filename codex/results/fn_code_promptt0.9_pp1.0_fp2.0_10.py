fn = lambda: None
# Test fn.__code__.co_filename
fn.__code__.co_filename = "filename.py"
# Test fn.__code__.co_firstlineno
fn.__code__.co_firstlineno = 1
# Test fn.__code__.co_flags
fn.__code__.co_flags = 1
# Test fn.__code__.co_lnotab
fn.__code__.co_lnotab = "01"

import sre_codes

# Test sre_codes.ATCODES
sre_codes.ATCODES = sre_codes.ATCODES

class CustomDataDescriptor:
    pip = 0

class CustomDescriptors:
    __slots__ = ()
    _pip_find_links = None
    # Pick up the kernel of test_descr.
    def __getattribute__(self, attr):
        descr = type(self).__dict__[attr]
        return object.__getattribute__(self, attr)
    def __setattr__(self, attr, value):

