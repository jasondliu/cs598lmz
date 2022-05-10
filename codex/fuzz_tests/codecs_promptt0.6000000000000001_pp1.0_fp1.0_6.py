import codecs
# Test codecs.register_error
def test_register_error():
    # The following test doesn't make sense on PyPy, because we don't
    # have the same weird implementation of codecs.
    if '__pypy__' in sys.builtin_module_names:
        py.test.skip("not relevant on PyPy")
    #
    def raise_exception(exc):
        def inner(exc):
            raise exc
        return inner
    def return_replacement(repl):
        def inner(exc):
            return (repl, len(exc.object))
        return inner
    def return_replacement_and_exception(repl):
        def inner(exc):
            return (repl, len(exc.object))
        return inner
    def raise_exception_and_ignore_len(exc):
        def inner(exc):
            raise exc
        return inner
    def return_replacement_and_ignore_len(repl):
        def inner(exc):
            return (repl, 1)
        return inner
    #
    # Test that registering a new error handler works
    codecs
