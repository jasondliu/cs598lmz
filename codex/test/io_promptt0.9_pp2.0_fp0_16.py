import io
# Test io.RawIOBase.

# This test checks that all read(), write() methods behave identically
# to those implemented by open().  Rather than checking implementation
# details, this test relies on the user operating on buffered data.

# Check read(), read1(), readall()
import _io

# A class inheriting from io.RawIOBase is required.
# Only the abstract methods will be called.
