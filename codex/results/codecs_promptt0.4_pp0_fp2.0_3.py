import codecs
# Test codecs.register_error
def my_error_handler(exception):
    print("my_error_handler:", exception)
    return ("?", exception.start + 1)
codecs.register_error("my_error", my_error_handler)

# Test UnicodeEncodeError
print("UnicodeEncodeError:")
for encoding in ["ascii", "latin-1", "my_error"]:
    try:
        print("{}: {}".format(encoding, "pymotw".encode(encoding)))
    except UnicodeEncodeError as err:
        print("ERROR:", err)

# Test UnicodeDecodeError
print("\nUnicodeDecodeError:")
for encoding in ["ascii", "latin-1", "my_error"]:
    try:
        print("{}: {}".format(encoding, b"abcd".decode(encoding)))
    except UnicodeDecodeError as err:
        print("ERROR:", err)

# Test UnicodeTranslateError
print("\nUnicodeTranslateError:")
for encoding
