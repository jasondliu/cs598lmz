import codecs
# Test codecs.register_error
import encodings.idna

# Test codecs.lookup
import encodings.utf_8

# Test codecs.open
f = codecs.open("test.txt", "r", "utf-8")
f.read()
f.close()

# Test codecs.EncodedFile
f = open("test.txt", "r")
ef = codecs.EncodedFile(f, "utf-8", "utf-16")
ef.read()
ef.close()

# Test codecs.StreamReader
sr = codecs.StreamReaderWriter(f, "utf-8", "utf-16", "strict")
sr.read()
sr.close()

# Test codecs.StreamWriter
sw = codecs.StreamReaderWriter(f, "utf-8", "utf-16", "strict")
sw.write("test")
sw.close()

# Test codecs.iterencode
def f(s):
    print s
for s in codecs.iterencode("test", "utf-8"):
    f(s)
