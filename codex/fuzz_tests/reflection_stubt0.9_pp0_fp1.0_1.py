fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi  # type: ignore
fn()

gen = (i for i in ())
fn.__code__ = gen.gi_frame.f_code  # type: ignore
fn()

# Finalize tests.
operations = (str,)
for operation in operations:
    gc.collect()
    object.__delattr__(fn, '__code__')
    gc.collect()

    with pytest.raises(ValueError):
        operation(fn())


def test_unicode_in_debug_names():
    if sys.version_info < (3, 6):
        return

    def emoji_function(): pass
    with pytest.raises(ValueError):
        inspect.signature(emoji_function)

    def emoji_function():
        """
        :param \u2764:
        :return:
        """
        pass
    with pytest.raises(KeyError):
        inspect.signature(emoji_function)

    def unicode_function(): pass
    with pytest.raises(ValueError):
        inspect.sign
