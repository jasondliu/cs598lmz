fn = lambda: None
# Test fn.__code__.co_firstlineno, fn.__code__.co_stacksize,
# fn.__code__.co_flags, fn.__code__.co_filename, fn.__code__.co_name,
# fn.__code__.co_varnames, fn.__code__.co_argcount, fn.__code__.co_consts,
# fn.__code__.co_names, fn.__code__.co_lnotab, fn.__code__.co_cellvars


if __name__ == "__main__":
    import __hello__
    assert __hello__.__hello__() == 'Hello world!', "function doesn't work"
    assert __hello__.__name__ == '__hello__', "function doesn't work"
    assert __hello__.__dict__['__hello__'].__name__ == '__hello__', "function doesn't work"
    print("function works! " + __hello__.__hello__())

    import __hello__function__
    assert __hello__function__.__hello_function__
