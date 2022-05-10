import codecs
# Test codecs.register_error

def handler(exception):
    print 'handler called'
    return (u'', exception.end)

codecs.register_error('test.my_handler', handler)

# encode
for encoding in ['ascii', 'iso8859-1']:
    print '- Encoding:', encoding
    try:
        s = unicode('\u0378', 'raw-unicode-escape').encode(encoding, 'test.my_handler')
    except UnicodeEncodeError, detail:
        print 'UnicodeEncodeError:', detail
    else:
        print 's =', s

# decode
for encoding in ['ascii', 'iso8859-1']:
    print '- Decoding:', encoding
    try:
        s = '\xff'.decode(encoding, 'test.my_handler')
    except UnicodeDecodeError, detail:
        print 'UnicodeDecodeError:', detail
    else:
        print 's =', s

# Test codecs.lookup_error

def handler(ex
