import codecs
# Test codecs.register_error()
import binascii

def hexlify(s):
    return binascii.hexlify(s).decode('ascii')

def unhexlify(s):
    return binascii.unhexlify(s.encode('ascii'))

def hexstr(s):
    return ' '.join([hex(ord(c))[2:] for c in s])

def hexstr2(s):
    return ' '.join([hex(ord(c))[2:].zfill(2) for c in s])

def hexstr3(s):
    return ' '.join([hex(ord(c))[2:].zfill(3) for c in s])

def hexstr4(s):
    return ' '.join([hex(ord(c))[2:].zfill(4) for c in s])

def hexstr5(s):
    return ' '.join([hex(ord(c))[2:].zfill(5) for c in s])

def hexstr6(s):
    return
