import codecs
# Test codecs.register_error()

import codecs

def my_error_handler(exception):
    print("my_error_handler:", exception)
    return (u'', exception.end)

codecs.register_error("test.my_error_handler", my_error_handler)

for encoding in ["ascii", "latin-1", "utf-8"]:
    print("Encoding:", encoding)
    try:
        print(codecs.decode("abc\xff", encoding, "test.my_error_handler"))
    except UnicodeDecodeError as err:
        print("ERROR:", err)

# Encoding: ascii
# my_error_handler: 'ascii' codec can't decode byte 0xff in position 3: ordinal not in range(128)
# u'abc'
# Encoding: latin-1
# my_error_handler: 'latin-1' codec can't decode byte 0xff in position 3: ordinal not in range(256)
# u'abc\xff'
# Encoding: utf-8
#
