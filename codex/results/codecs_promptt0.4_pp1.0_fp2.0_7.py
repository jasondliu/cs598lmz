import codecs
# Test codecs.register_error

def handler(exception):
    print("handler called:", exception)
    return ("<%s>" % exception.object[exception.start:exception.end],
            exception.end)

for name in ["iso8859_7", "cp1253", "koi8_r", "cp874", "iso8859_11"]:
    codecs.register_error(name, handler)
    print(name, ":", codecs.decode("\x80\x81\x82\x83\x84\x85\x86\x87\x88\x89\x8a\x8b\x8c\x8d\x8e\x8f\x90\x91\x92\x93\x94\x95\x96\x97\x98\x99\x9a\x9b\x9c\x9d\x9e\x9f\xa0\xa1\xa2\xa3\xa4\xa5\xa6\xa7\xa8\xa9\xaa\x
