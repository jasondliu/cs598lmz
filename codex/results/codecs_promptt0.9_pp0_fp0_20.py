import codecs
# Test codecs.register_error()
def unknow_codec(exc):
    return '{}{}{}{}{}{}{}{}{}{}{}{}'.format(exc.object[0],
                                            exc.object[1],
                                            exc.object[2],
                                            exc.object[3],
                                            exc.object[4],
                                            exc.object[5],
                                            exc.object[6],
                                            exc.object[7],
                                            exc.object[8],
                                            exc.object[9],
                                            exc.object[10],
                                            exc.object[11])
codecs.register_error('unknown-codec', unknow_codec)
test_data = '\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0A\x0B'
# codecs.encode(test_data, 'unknown-codec')
# Traceback (most recent call last):
#   File "<pyshell#14>", line 1, in <
