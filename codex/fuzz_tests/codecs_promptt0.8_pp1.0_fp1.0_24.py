import codecs
# Test codecs.register_error
f = codecs.open("nonexist.txt",encoding='iso8859-1',errors='replace')
print f.readline()

# Test io.open
f = io.open("nonexist.txt",encoding='iso8859-1')
print f.readline()


# Test encoding
#print f.encoding
#print codecs.lookup(f.encoding).name
#print codecs.lookup(f.encoding).encode('中文')
