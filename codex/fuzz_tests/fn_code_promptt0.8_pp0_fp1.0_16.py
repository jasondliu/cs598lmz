fn = lambda: None
# Test fn.__code__.co_filename
# Test fn.__code__.co_firstlineno
# Test fn.__code__.co_flags
# No __code__.co_lnotab test.
# Test fn.__code__.co_name
# Test fn.__code__.co_names
# Test fn.__code__.co_nlocals
# Test fn.__code__.co_stacksize
# Test fn.__code__.co_varnames


# cp56710
def f56710():
    """Docstring for function 'f56710'"""
    pass


# Protected and public attributes should not be expanded.
# Test f56710.__doc__
# Protected and public attributes should not be expanded.
# Test f56710.__module__
# Test f56710.__name__
# Test f56710.func_closure
# Test f56710.func_code
# Test f56710.func_defaults
# Test f56710.func_dict
# Test f56710.func_doc
