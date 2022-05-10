from lzma import LZMADecompressor
LZMADecompressor().decompress(b"")
b'\x00\x00\x00\x01\xff\xff'
b'\0\0\0\1\xff\xff'
'''
def Binary1(v):
    assert v>=0 and v<=MAX_BINARY
    v=(v<<2)|1
    if v<=255: return chr(v)
    if v<=65535: return (chr(v&255)+chr(v>>8))
    return chr(v&255)+chr((v>>8)&255)+chr((v>>16)&255)+chr((v>>24))

def IntStr1(*args):
    i=map(Binary1,args)
    i=list(i)
    i.insert(0,chr(len(i)))
    return "".join(i)

def ParseBinary1(i,last=len(i)):
    assert last>0
    assert i[0]!=chr(0)
    if i[0]==chr
