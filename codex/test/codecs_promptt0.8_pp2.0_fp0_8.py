import codecs
# Test codecs.register_error()
# codecs.register_error()

# Test codecs.lookup()
# codecs.lookup()

# Test codecs.lookup_error()
# codecs.lookup_error()


## Test utf-7 codec
# Test transliterate error handler (requires python 2.4)

def print_test_utf7_encode(errors, input, output):
    try:
        encoded = codecs.utf_7_encode(input, errors)
    except:
        encoded = 'error'
