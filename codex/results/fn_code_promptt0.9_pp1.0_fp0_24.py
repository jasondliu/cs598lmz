fn = lambda: None
# Test fn.__code__.__getattribute__('co_argcount')
# TODO: get a Python 4 test


def test_lookup():
    # Test .lookup()
    mod = types.ModuleType("foo")
    space = sys.__frame.f_code.co_names
    assert "space" == mod.__dict__.lookup("space")
    assert "__code__" == mod.__dict__.lookup("__code__")
    assert None is mod.__dict__.lookup("fn")


def test_new_class_inherit_set_keywords():
    # Test _PySet_New() calls for _PyObjectDict_NewPresized()
    # Test dict creation with dict.__init__()
    class Base:
        def __init__(self, base, **kwds):
            super().__init__()
            self.__dict__.update(kwds)
        def __setattr__(self, key, value):
            self.__dict__[key] = value

    class C(Base):
        def __init__(self
