fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.send

result = fn()  # Should not crash python


@pytest.mark.xfail(sys.version_info[:2] == (3, 7),
                   reason='https://bugs.python.org/issue35247')
def test_send_send():
    """Test that send can be called twice on a generator.
    http://bugs.python.org/issue15016
    """
    def fn(a, b, c):
        try:
            yield a
            yield b
            yield c
        except StopIteration as e:
            pass
    gen = fn(1, 2, 3)
    next(gen)
    gen.send(10)
    gen.send(20)


def test_instant_generators():
    """Ensure that code objects with a parameter named 'is_coroutine' are not
    treated as generators.

    https://bugs.python.org/issue29256
    """

    def gen():
        yield

    # Using type(<expr>)(...), rather than <expr>(...), ensures that
    # cor
