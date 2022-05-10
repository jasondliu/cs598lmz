import codecs
# Test codecs.register_error()

# First define the error handling function
def my_handler2(exception):
    # Get the start and end of the exception
    tb = exception.__traceback__
    start = tb.tb_frame.f_locals["start"]
    end = tb.tb_frame.f_locals["end"]

    # Replace the bad characters with \xXX
    s = []
    for c in range(start, end):
        try:
            char = exception.object[c]
        except IndexError:
            char = "\x00"
        s.append("\\x%02x" % ord(char))
    return "".join(s), end

# Now register it
codecs.register_error("my_handler", my_handler2)

# Encode our test string
encoded = "Hello world".encode("ascii", "my_handler")
