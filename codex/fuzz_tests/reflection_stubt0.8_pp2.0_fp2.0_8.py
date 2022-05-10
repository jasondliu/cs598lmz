fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
del gi, fn"""
        # Same as above, but don't del gi. Since it's a generator, deleting it
        # causes its code object to be freed.
        src="""fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi"""
        assert check_py3k_warnings(src, False, False)

        src="""fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
del gi"""
        assert check_py3k_warnings(src, False, True)

        src="""if 1:
    fn = lambda: None
    fn.__code__.co_code = b"abc"
else:
    fn = lambda: None
    gi = (i for i in ())
    fn.__code__ = gi"""
        assert not check_py3k_warnings(src, False, True)

        src="""if 1:
    fn = lambda: None
    fn.__code__ = (1 for i in ())
else:

