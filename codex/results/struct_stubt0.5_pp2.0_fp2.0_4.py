from _struct import Struct
s = Struct.__new__(Struct)
s.format = '<I'
s.size = 4

def p(x):
    return s.pack(x)

def u(x):
    return s.unpack(x)[0]

def xor(x, y):
    return ''.join(chr(ord(a) ^ ord(b)) for a, b in zip(x, y))

def pad(s):
    return s + '\x00' * (-len(s) % 4)

def encrypt(key, message):
    message = pad(message)
    return xor(key, message)

def decrypt(key, message):
    return xor(key, message)

def get_flag(key):
    return decrypt(key, FLAG)

def main():
    print '''
    Welcome to my super secure messaging service.
    Please enter your key.
    '''
    key = raw_input()
    print '''
    Now enter your message.
    '''
    message = raw_input()
    print '''
    Your encrypted message is
