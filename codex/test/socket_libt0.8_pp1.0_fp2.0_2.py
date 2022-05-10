import socket

from cryptography.hazmat.backends import default_backend
from cryptography.x509 import load_pem_x509_certificate

host = 'localhost'
port = 8000
ADDR = (host, port)
BUFSIZE = 4096

file_path = './SSL/ssl.crt'

with open(file_path, 'r') as f:
    csr = f.read()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(ADDR)

s.sendall(csr.encode())

cert_pem = s.recv(BUFSIZE)

certificate = load_pem_x509_certificate(
    cert_pem, default_backend())

public_key = certificate.public_key()

cert_serial_number = certificate.serial_number

