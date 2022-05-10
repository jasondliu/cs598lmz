import signal
# Test signal.setitimer
signal.setitimer(signal.ITIMER_REAL, 0.01, 0.01)
signal.setitimer(signal.ITIMER_VIRTUAL, 0.01, 0.01)
signal.setitimer(signal.ITIMER_PROF, 0.01, 0.01)

import socket
# Test socket.inet_aton
socket.inet_aton("127.0.0.1")

import _ssl
# Test _ssl.PROTOCOL_SSLv23
_ssl.PROTOCOL_SSLv23

# Test _ssl.OPENSSL_VERSION_NUMBER
_ssl.OPENSSL_VERSION_NUMBER

# Test _ssl.OPENSSL_VERSION
_ssl.OPENSSL_VERSION

# Test _ssl.HAS_SNI
_ssl.HAS_SNI

# Test _ssl.HAS_ECDH
_ssl.HAS_ECDH

# Test _ssl.HAS_NPN
_ssl.HAS_NPN

# Test _ssl.H
