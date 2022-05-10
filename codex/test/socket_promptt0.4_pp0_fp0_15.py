import socket
# Test socket.if_indextoname()
try:
    socket.if_indextoname(1)
except OSError as e:
    if e.errno != errno.ENXIO:
        raise
    print("SKIP")
    raise SystemExit

import uasyncio as asyncio
import uasyncio.core
import usocket as _socket
import ussl as ssl
import ussl.ssl_axtls as ssl_axtls
import ussl.ssl_mbedtls as ssl_mbedtls
import uerrno
import ubinascii
import utime
import gc
import uhashlib
import uos
import ujson
import ustruct
import uzlib
import uselect
import usys
import uctypes
import uheapq
import ubinascii
import ucollections
import ure
import uio
import ussl
import ussl.ssl_axtls
import ussl.ssl_mbedtls
import uctypes
import uheapq
import ucollections
import ure
import uio

