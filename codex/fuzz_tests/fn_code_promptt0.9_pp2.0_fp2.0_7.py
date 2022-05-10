fn = lambda: None
# Test fn.__code__.co_flags to detect when we need to re-compile a
# code object with new flags.
def func_flags(func):
    try:
        return func.__code__.co_flags
    except AttributeError:
        pass
    try:
        return func.func_code.co_flags
    except AttributeError:
        # This can occur in restricted mode
        pass
    return 0


def update_code_location(old_code, new_code):
    if hasattr(old_code, 'co_filename'):
        new_code = CodeType(new_code.co_argcount,
                            new_code.co_nlocals,
                            new_code.co_stacksize,
                            new_code.co_flags,
                            new_code.co_code,
                            new_code.co_consts,
                            new_code.co_names,
                            new_code.co_varnames,
                            old_code.co_filename,
                            old_code.co_name,
                
