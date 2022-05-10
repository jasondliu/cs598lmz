import codecs
# Test codecs.register_error() 
import codecs

def decimalrepair(error):
    a = bytearray()
    for i in error.object[error.start:error.end]:
        a.append(int(i))
    return (a, error.end)

codecs.register_error("decimalincorrect", decimalrepair)

with open("gumek.txt", 'rb') as f:
    text = f.read()
    print(text)
    pass
#print(codecs.decode(text, "ascii", "decimalincorrect").decode("utf-8"))
#print(codecs.open("gumek.txt", 'rb'))
