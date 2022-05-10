import codecs
# Test codecs.register_error

def handler(exception):
    print("handler:", exception)
    return ("\x00", exception.end)

codecs.register_error("test.lookup", handler)

# Test a lookup error
print("\n*** Lookup error:")
codecs.lookup_error("test.lookup")

# Test a UnicodeEncodeError
print("\n*** UnicodeEncodeError:")
