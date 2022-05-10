import io
# Test io.RawIOBase.readinto()

# Test readinto() on a RawIOBase object
#
# This test checks that readinto() behaves as expected on a RawIOBase object.
# It checks the following:
#   - readinto() returns the number of bytes read
#   - readinto() raises an IOError if the object is closed
#   - readinto() raises an IOError if the object is in non-blocking mode
#   - readinto() raises an IOError if the object is in write mode
#   - readinto() raises an IOError if the object is in append mode
#   - readinto() raises an IOError if the object is in read/write mode
#   - readinto() raises an IOError if the object is in append/read/write mode
#   - readinto() raises a ValueError if the buffer is not writable
#   - readinto() raises a TypeError if the buffer is not a writable buffer
#   - readinto() raises a TypeError if the offset is not an integer
#   - readinto() raises a TypeError if the offset is not an integer
#   - readinto() raises a
