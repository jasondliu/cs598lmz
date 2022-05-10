import io
# Test io.RawIOBase

# Test that an instance of a subclass of RawIOBase can be created.
# (This tests the default implementations of the abstract methods.)
r = io.RawIOBase()

# Test that the default implementations work
r.close()
r.closed
