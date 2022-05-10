import socket, traceback, struct
import time
import ecdsa

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
s.bind(("192.168.10.5", 37020))

secKey = os.urandom(32)
pubKey = ecdsa.SigningKey.from_string(secKey, curve=ecdsa.SECP256k1).get_verifying_key()

print('secKey: ', str(secKey))
print('pubKey: ', pubKey)
print('pubKey: ', bytes.decode(str(pubKey)))


while 1:
    try:
        message, address = s.recvfrom(8192)
        print("Got data from", address)
        # Acknowledge it.
        #s.sendto("We got: %s" %
