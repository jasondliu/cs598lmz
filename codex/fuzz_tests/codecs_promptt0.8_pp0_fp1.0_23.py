import codecs
# Test codecs.register_error() by registering an error handler that
# counts the number of times an error handler is called.
global callback_count
callback_count = 0

def unichr_error_handler(exception):
    global callback_count
    callback_count += 1
    print(">>>", repr(callback_count), repr(exception))
    return (("%d" % exception.object).encode("ascii"), exception.start + 1)
# Check that a bad character U+FFFD is returned for each invalid
# character in the UTF-16 input.

codecs.register_error("test.unichr", unichr_error_handler)

for data in [b"\xff\xfe", b"\xff\xfe\x41\x41", b"\xff\xfe\x00\x01\x00\x02\x00\x03\x00\x04", b"\xff\xfe\xd8\x01\x01\xdc\x01\x01", b"\xff\xfe\xd8\x01\x01\x
