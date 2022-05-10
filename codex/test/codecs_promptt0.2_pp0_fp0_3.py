import codecs
# Test codecs.register_error()

import codecs

def handler(exception):
    print('[%s] %s' % (exception.__class__.__name__, exception))
    return '', exception.end

codecs.register_error('test.ignore', handler)
codecs.register_error('test.replace', handler)
codecs.register_error('test.xmlcharrefreplace', handler)
codecs.register_error('test.backslashreplace', handler)

for encoding in ['ascii', 'latin-1', 'utf-8', 'utf-16']:
    print('Encoding:', encoding)
    for errors in ['ignore', 'replace', 'xmlcharrefreplace', 'backslashreplace']:
        print('Error handler:', errors)
        print(codecs.encode('abc\x80def', encoding, errors='test.' + errors))

# Test codecs.register_error()

import codecs

