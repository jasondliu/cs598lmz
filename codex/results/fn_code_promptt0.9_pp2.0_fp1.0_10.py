fn = lambda: None
# Test fn.__code__.co_nlocals
def nlocals_fn():
    nlocals1_fn()
def nlocals2_fn():
    nlocals3_fn()
# Test fn.__code__.co_varnames
const_fn = lambda: 257 # Test fn.__code__.co_consts
# Test fn.__code__.co_names
empty_fn = (lambda: ()) # Test fn.__code__.co_flags
def kwargs_fn(*args, **kwargs):
    return args, kwargs

class MethodClass:
    # Test fn.__code__.co_filename
    def filename_method(self):
        filename1_fn()
    # Test fn.__code__.co_name
    def name_method(self):
        name1_fn()
    # Test fn.__code__.co_firstlineno
    def firstline_method(self):
        firstline1_fn()
    # Test fn.__code__.co_lnotab
    def lnotab_method(self):
        l
