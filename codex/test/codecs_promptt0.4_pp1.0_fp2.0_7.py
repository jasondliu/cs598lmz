import codecs
# Test codecs.register_error

def handler(exception):
    print("handler called:", exception)
    return ("<%s>" % exception.object[exception.start:exception.end],
            exception.end)

for name in ["iso8859_7", "cp1253", "koi8_r", "cp874", "iso8859_11"]:
    codecs.register_error(name, handler)
