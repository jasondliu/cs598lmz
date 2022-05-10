import codecs
# Test codecs.register_error
with codecs.open('/tmp/test.txt', 'w', 'utf-8', errors='errorhandler') as f:
    f.write('\udc80')

with codecs.open('/tmp/test.txt', 'r', 'utf-8', errors='errorhandler') as f:
    print(f.read())

with codecs.open('/tmp/test.txt', 'r', 'utf-8', errors='ignore') as f:
    print(f.read())
    
with codecs.open('/tmp/test.txt', 'r', 'utf-8', errors='replace') as f:
    print(f.read())

with codecs.open('/tmp/test.txt', 'r', 'utf-8', errors='strict') as f:
    print(f.read())

with codecs.open('/tmp/test.txt', 'r', 'utf-8', errors='backslashreplace') as f:
    print(f.read())

with codecs.open('/tmp/test.txt', 'r',
