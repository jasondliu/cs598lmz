import codecs
# Test codecs.register_error:
import os

def dummy_error_handler(exception):
    if isinstance(exception, ValueError):
        print('dummy_error_handler:', exception)
        return '', exception.end
    else:
        raise exception
codecs.register_error('test.dummy', dummy_error_handler)
codecs.encode('abc\uDC80def', 'ascii', 'test.dummy')
codecs.encode('abc\uDC80def', 'ascii', 'test.dummy')
# UnicodeEncodeError: 'ascii' codec can't encode character '\udc80' in position
# 3: ordinal not in range(128)

#        codecs.decode('abc\x80def', 'ascii', 'test.dummy')
# UnicodeDecodeError: 'ascii' codec can't decode byte 0x80 in position 3:
# ordinal not in range(128)

