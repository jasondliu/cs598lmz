import codecs
# Test codecs.register_error

import codecs

def handler(exception):
    print 'handler called'
    return (u'', exception.end)

codecs.register_error('test.lookup', handler)

u = u'\u3042\u3044\u3046\u3048\u304a'

for encoding in ('euc_jp', 'iso2022_jp', 'shift_jis'):
    print encoding
    print codecs.getencoder(encoding)(u, 'test.lookup')
    print codecs.getdecoder(encoding)('\xa1\xa1\xa1\xa1\xa1', 'test.lookup')
    print codecs.getincrementalencoder(encoding)('test.lookup')
    print codecs.getincrementaldecoder(encoding)('test.lookup')

print 'registering again'
codecs.register_error('test.lookup', handler)

for encoding in ('euc_jp', 'iso2022_jp', 'shift_jis'):
   
