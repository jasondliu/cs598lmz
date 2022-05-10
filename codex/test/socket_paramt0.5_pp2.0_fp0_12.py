import socket
socket.if_indextoname(socket.if_nametoindex('lo'))

socket.if_nametoindex('lo')

import socket
from socket import AF_INET, SOCK_STREAM, SOCK_DGRAM
from socket import socket as Socket
from socket import gethostbyname as GetHostByName
from socket import gethostname as GetHostName
from socket import gethostbyaddr as GetHostByAddr
from socket import gethostbyname_ex as GetHostByNameEx
from socket import getprotobyname as GetProtoByName
from socket import getprotobynumber as GetProtoByNumber
from socket import getservbyname as GetServByName
from socket import getservbyport as GetServByPort
from socket import getaddrinfo as GetAddrInfo
from socket import getnameinfo as GetNameInfo
from socket import getdefaulttimeout as GetDefaultTimeout
from socket import setdefaulttimeout as SetDefaultTimeout
from socket import getfqdn as GetFQDN
from socket import create_connection as CreateConnection
import os
import sys
import time
import string
import struct
import select
import re

