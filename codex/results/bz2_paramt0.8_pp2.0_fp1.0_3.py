from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(mem).decode('utf8')

s = """
import socket,struct,os,binascii,base64

def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(random.random() * 0.1)

def finish(s):
    slowprint('Access Granted.')
    os.system('/bin/sh')

def reject():
    slowprint('Acess Denied.')
    os.abort()

def get_flag(s):
    return s.recv(1024)

def convert_to_network(host_order_bytes):
    return struct.pack("!I", socket.htonl(host_order_bytes))

def p32(x):
    return struct.pack('<I', x)

def u32(x):
    return struct.unpack('<I', x)[0]

if os.fork():
    exit(0)

slowprint('Welcome to
