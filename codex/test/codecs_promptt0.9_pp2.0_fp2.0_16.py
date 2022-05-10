import codecs
# Test codecs.register_error() 
import codecs

def decimalrepair(error):
    a = bytearray()
    for i in error.object[error.start:error.end]:
        a.append(int(i))
    return (a, error.end)

codecs.register_error("decimalincorrect", decimalrepair)

