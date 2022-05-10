import io
# Test io.RawIOBase class compatibility.
test_support.verify_api(io.RawIOBase, io.IOBase)

class TestRawIOBase:
    def test_readinto(self):
        # Test that readinto can be implemented in terms of read.
        io = _FakeIO()
        io.read_data = "some"
        buffer = bytearray(3)
        ret = io.readinto(buffer)
        self.assertEqual(ret, 3)
        self.assertEqual(buffer, "som")

class StreamTests(base_io.StreamTests):
    # subclass StreamTests to add the RawIOBase constructor test

    def test_constructor(self):
        # Each concrete RawIO implementation must have a constructor
        # that accepts a single positional argument, "raw", that is
        # an object (typically, another RawIOBase implementation) from
        # which the new RawIO implementation will read or write.
        #
        # The constructor must *not* close the raw implementation upon
        # exit if all is well.

        import io
        myio =
