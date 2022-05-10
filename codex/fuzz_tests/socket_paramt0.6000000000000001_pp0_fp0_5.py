import socket
socket.if_indextoname(2)

print(socket.gethostbyaddr("192.168.1.1"))

print(socket.getservbyport(53, 'udp'))
print(socket.getservbyport(53, 'tcp'))

import ssl

ctx = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
ctx.load_verify_locations('ca-bundle.crt')

s = ctx.wrap_socket(socket.socket(), server_hostname='www.python.org')
s.connect(('www.python.org', 443))
cert = s.getpeercert()

print(cert)

import sys
import os

print('sys.argv[0] =', sys.argv[0])
print('os.getcwd() =', os.getcwd())

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('host')
parser.add_argument('-p', '--port', type=int, default=80)
args = parser
