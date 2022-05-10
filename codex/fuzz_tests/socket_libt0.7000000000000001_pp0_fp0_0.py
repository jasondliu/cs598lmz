import socket
import ssl
import sys
import time

from OpenSSL import crypto


def gen_pem(name):
    pk = crypto.PKey()
    pk.generate_key(crypto.TYPE_RSA, 2048)
    cert = crypto.X509()
    cert.set_pubkey(pk)
    cert.sign(pk, 'sha256')
    open(name + '.key', 'w').write(crypto.dump_privatekey(crypto.FILETYPE_PEM, pk))
    open(name + '.crt', 'w').write(crypto.dump_certificate(crypto.FILETYPE_PEM, cert))


class TestServer(object):
    def __init__(self):
        self.sock = socket.socket()
        self.sock.bind(('', 0))
        self.sock.listen(1)
        self.port = self.sock.getsockname()[1]
        self.ctx = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH
