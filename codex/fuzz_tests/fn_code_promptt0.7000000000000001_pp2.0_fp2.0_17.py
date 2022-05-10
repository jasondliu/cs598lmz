fn = lambda: None
# Test fn.__code__
func_code_fn.__code__

# Test fn.__code__.__class__
func_code_fn.__code__.__class__

# Test code(fn)
code(func_code_fn)

# Test code(fn).__class__
code(func_code_fn).__class__

# Test fn.__code__.co_argcount
func_code_fn.__code__.co_argcount

# Test fn.__code__.co_argcount.__class__
func_code_fn.__code__.co_argcount.__class__

# Test code(fn).co_argcount
code(func_code_fn).co_argcount

# Test code(fn).co_argcount.__class__
code(func_code_fn).co_argcount.__class__

# Test fn.__code__.co_argcount()
func_code_fn.__code__.co_argcount()

# Test fn.__code__.co_argcount().__class__
func_code_
