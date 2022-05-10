import select
# Test select.select
select.select( [], [], [] )

import socket
socket.getaddrinfo( "", "" )

import ssl
ssl.CERT_NONE
ssl.PROTOCOL_TLSv1
ssl.OP_NO_SSLv2
ssl.OP_NO_SSLv3
ssl.OP_NO_COMPRESSION
ssl.OP_SINGLE_DH_USE
ssl.OP_SINGLE_ECDH_USE
ssl.OP_CIPHER_SERVER_PREFERENCE
ssl.OP_NO_TICKET
ssl.OP_NO_TLSv1_1
ssl.OP_NO_TLSv1_2

# Test ssl.create_default_context
context = ssl.create_default_context()
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE
context.options |= ssl.OP_NO_SSLv2
context.options |= ssl.OP_NO_SSLv3
context.options |= ssl.OP_NO_COMPRESSION

