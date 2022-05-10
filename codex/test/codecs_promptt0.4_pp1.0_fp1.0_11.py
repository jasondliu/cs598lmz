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
