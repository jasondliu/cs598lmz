import _struct
import _socket
from common import *
from ctime import time
from socket import socket, IPPROTO_IP, IP_TTL, SOCK_RAW, SOCK_DGRAM, SOCK_STREAM, IPPROTO_UDP
from socket import IPPROTO_TCP, IPPROTO_ICMP, gethostbyname, gethostname
from socket import inet_ntoa, inet_aton
from socket import error as socket_error
from gevent import socket as gsocket
from gevent.server import DatagramServer
from gevent.server import StreamServer
from gevent import monkey; monkey.patch_all()

from dnslib import DNSRecord, RR, A
from dnslib.server import DNSServer,DNSHandler,BaseResolver,DNSLogger

from Crypto.Hash import MD5
from Crypto.Hash import SHA
from Crypto.Cipher import AES
from Crypto import Random
from Crypto.Random import random
from Crypto.Util.number import bytes_to_long, long_to_bytes
from Crypto.PublicKey import RSA

from struct import pack, un
