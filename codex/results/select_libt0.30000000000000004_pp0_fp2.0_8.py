import select
import socket
import struct
import sys
import threading
import time
import traceback

from . import util
from . import version
from . import xlog

logger = xlog.getLogger("tunnel")

# https://github.com/shadowsocks/shadowsocks/blob/master/shadowsocks/crypto/openssl.py
# https://github.com/shadowsocks/shadowsocks/blob/master/shadowsocks/crypto/table.py
# https://github.com/shadowsocks/shadowsocks/blob/master/shadowsocks/crypto/salsa20.py
# https://github.com/shadowsocks/shadowsocks/blob/master/shadowsocks/crypto/aead.py
# https://github.com/shadowsocks/shadowsocks/blob/master/shadowsocks/crypto/rc4_md5.py
# https://github.com/shadowsocks/shadowsocks/blob/master/shadowsocks/crypto/chacha20_poly1305.py
#
