import lzma
# Test LZMADecompressor by decompressing some data:
#print(lzma.decompress(urllib.request.urlopen('http://www.python.org').read()))

import socket
import ssl
import pprint

#create an INET, STREAMing socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('mail.python.org', 443))
print(s)

w = ssl.wrap_socket(s, ssl_version=ssl.PROTOCOL_SSLv23)
print(w)

print(pprint.pformat(w.getpeercert()))
print(w.cipher())

w.write(b'GET / HTTP/1.1\r\nHost: mail.python.org:443\r\n\r\n')
w.close()
