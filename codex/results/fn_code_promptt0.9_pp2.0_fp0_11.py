fn = lambda: None
# Test fn.__code__.co_firstlineno
test_fn.__code__.co_firstlineno == 1

# Test firstlineno of fn_with_docstring
fn_with_docstring.__code__.co_firstlineno == 1

# Test firstlineno of empty_code
mod = fn.__code__.co_firstlineno
mod2 = nonlocal_code.co_firstlineno

# Test firstlineno of fn_with_docstring
module_lineno = mod.co_firstlineno
module_lineno2 = mod2.co_firstlineno
"'''
