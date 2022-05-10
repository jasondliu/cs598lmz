import codecs
# Test codecs.register_error()

# Output version number to stdout
print(sys.version)

# Test codecs.register_error()
# In the error callback, substitute the first character with "?"
def err_handler(exception):
    return (u"?", exception.start + 1)
codecs.register_error("test", err_handler)

# Test encodings
for encoding in ('ascii', 'latin-1', 'utf-8'):
    print(encoding)
    # Only ascii should work, the others should give UnicodeEncodeError
    try:
        encoded = input.encode(encoding, 'test')
    except UnicodeEncodeError:
        encoded = None
    # Print a ? for each bad character
    if encoded is not None:
        print(encoded.decode(encoding))
    else:
        print(repr(input))
    print()
</code>
See here for the official Python documentation on codecs.

