import codecs
# Test codecs.register_error()
#
# The UTF-7 encoder and decoder are now registered as error handlers for
# the UTF-7 codec by default.

import codecs
import string

# Read UTF-7 from a file with a surrogatecodec error handler
def read_utf7_file(filename):
    f = open(filename, 'rb')
    d = f.read()
    f.close()
    # Decode with surrogateescape error handler enabled by default
    decoded = d.decode('utf-7')
    # Encode back to bytes with default error handler
    encoded = decoded.encode('utf-7')
    return d, decoded, encoded

def test():
    # Check that files with errors in them can still be decoded
    f1, d1, e1 = read_utf7_file('utf7.txt')
    f2, d2, e2 = read_utf7_file('utf7-2.txt')
    if f1 != e1 or f2 != e2:
        print('Error in UTF-7 error handlers')

def test_main
