fn = lambda: None
# Test fn.__code__.co_filename to detect frozen functions.
if hasattr(fn, '__code__'):
    fn_code_attr = '__code__'
elif hasattr(fn, 'func_code'):
    fn_code_attr = 'func_code'
else:
    raise RuntimeError("Could not find function code attribute!")
fn_code = getattr(fn, fn_code_attr)
if hasattr(fn_code, 'co_filename'):
    # No-op if fn is already frozen.
    if not hasattr(fn_code, 'co_freevars'):
        # Replace the function's code object with a frozen one.
        co = fn_code
        filename = co.co_filename
        if not filename.startswith("<") or not filename.endswith(">"):
            f = open(co.co_filename)
            sourcelines = f.readlines()
            f.close()
        else:
            sourcelines = None
        codeobj = _make_code(co.co_argcount, co.co_nloc
