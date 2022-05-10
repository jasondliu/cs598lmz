fn = lambda: None
# Test fn.__code__ exists
if hasattr(fn, '__code__'):
    import inspect
    # Test fn.__code__.co_flags exists
    if hasattr(inspect.currentframe().f_back.f_back.f_code, 'co_flags'):
        # Test fn.__code__.co_flags.no_stack_check exists
        if hasattr(fn.__code__, 'co_flags'):
            # Test fn.__code__.co_flags.no_stack_check exists
            if hasattr(fn.__code__.co_flags, 'no_stack_check'):
                # Test fn.__code__.co_flags.no_stack_check exists
                if hasattr(fn.__code__.co_flags.no_stack_check, '__call__'):
                    raise Exception('WTF')
                else:
                    # Test fn.__code__.co_flags.no_stack_check exists
                    if hasattr(fn.__code__.co_flags.no_stack_check, '__call__'):
                        raise
