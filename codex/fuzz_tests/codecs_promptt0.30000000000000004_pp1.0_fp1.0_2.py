import codecs
# Test codecs.register_error

def handler(exception):
    print exception
    return (u'', exception.end)

codecs.register_error('test.ignore', handler)

# test encoding

print '%r' % (u'\u3042\u3044'.encode('euc_jp', 'test.ignore'),)
print '%r' % (u'\u3042\u3044'.encode('euc_jp', 'test.ignore'),)
print '%r' % (u'\u3042\u3044'.encode('euc_jp', 'test.ignore'),)
print '%r' % (u'\u3042\u3044'.encode('euc_jp', 'test.ignore'),)
print '%r' % (u'\u3042\u3044'.encode('euc_jp', 'test.ignore'),)
print '%r' % (u'\u3042\u3044'.encode('euc_jp', 'test.ignore'),)
print '%r' % (u'\u
