import codecs
# Test codecs.register_error

class Test_register_error:

    # Codecs module tests
    # Test codecs.register_error

    def test_register_error(self):
        import codecs
        # Test codecs.register_error

        class X:
            def __init__(self, err):
                self.err = err
            def __call__(self, e):
                return (u"", e.end)
        codecs.register_error("test.x", X)
        codecs.register_error("test.y", X)

        assert codecs.lookup_error("test.x") is X
        assert codecs.lookup_error("test.y") is X
        assert codecs.lookup_error("test.z") is None
        try:
            codecs.register_error("test.y", X)
        except ValueError:
            pass
        else:
            raise TestFailed("did not raise ValueError on second register")

        class Y:
            pass
        try:
            codecs.register_error("test.z", Y)
       
