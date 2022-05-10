import codecs
# Test codecs.register_error()

import codecs

def search_function(encoding):
    if encoding == "test.searchfunction":
        return codecs.lookup("utf-8")
    return None

codecs.register(search_function)

def test(encoding):
    print '-'*20
    print 'Encoding :', encoding
    print 'Encoder  :', codecs.getencoder(encoding)
    print 'Decoder  :', codecs.getdecoder(encoding)
    print 'IncrementalEncoder  :', codecs.getincrementalencoder(encoding)
    print 'IncrementalDecoder  :', codecs.getincrementaldecoder(encoding)
    print 'StreamWriter  :', codecs.getwriter(encoding)
    print 'StreamReader  :', codecs.getreader(encoding)
    print 'StreamReaderWriter  :', codecs.getreader(encoding)
    print 'StreamRecoder  :', codecs.getreader(encoding)

for encoding in ["test.searchfunction", "test.searchfunction
