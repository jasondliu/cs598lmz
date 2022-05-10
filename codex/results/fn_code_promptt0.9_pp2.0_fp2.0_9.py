fn = lambda: None
# Test fn.__code__.co_flags, this is only available in python >= 2.7
if sys.version_info >= (2, 7):
    fn.__code__.co_flags = 0
    assert fn.getflags() == 0
    fn.__code__.co_flags = 1
    assert fn.getflags() == 1
    fn.__code__.co_flags = 32
    assert fn.getflags() == 32
    fn.__code__.co_flags = 33
    assert fn.getflags() == 33

# Test fn.__qualname__, this is only available in python >= 2.6
if sys.version_info >= (2, 6):
    fn.__qualname__ = 'Test.name'
    assert fn.get_full_name() == 'Test.name'
    assert fn.get_class_name() == 'Test'
    assert fn.get_funcname() == 'name'
    del fn.__qualname__
    fn.__name__ = 'hello'
    assert fn.get_full_name() == 'hello'
    assert fn.get
