import codecs
# Test codecs.register_error
with codecs.open(u'xxx.report', 'w', 'utf-8') as f:
    try:
        f.write(u'\xe4\xf6\xfc'.encode('latin1'))
    except UnicodeEncodeError:
        print('uft-8 could not encode latin1 data')

try:
    codecs.register_error('test.xmlcharrefreplace', codecs.xmlcharrefreplace_errors)
except LookupError:
    pass

with codecs.open(u'xxx.report', 'w', 'utf-8', errors='test.xmlcharrefreplace') as f:
    try:
        f.write(u'\xe4\xf6\xfc'.encode('latin1'))
    except UnicodeEncodeError:
        print('uft-8 could not encode latin1 data')
print('open the file xxx.report')
