fn = lambda: None
# Test fn.__code__.co_names and fn.co_names
    fn.__code__.co_names = ('name',)
    check_seq_types(fn.__code__, 'co_names', str)
    fn.__code__.co_names = (1,)
    check_seq_types(fn.__code__, 'co_names', int)

    fn.__code__.co_names = 1
    raises(TypeError, "fn.__code__.co_names = 1")

    f = compile("a", "", "eval")

    raises(TypeError, "f.__code__.co_names = lambda x: x")
    raises(TypeError, "f.__code__.co_names = (1, [1])")
    raises(TypeError, "f.__code__.co_names = ([1, 2],)")
    raises(TypeError, "f.__code__.co_names = 'cto8pvjry'")
    raises(TypeError, "f.__code__.co_names = (1+2j,)")
