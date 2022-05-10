import weakref

from gevent import monkey
monkey.patch_all()

from gevent.server import StreamServer
from gevent.queue import Queue

from gevent.socket import socket
from gevent.socket import AF_INET
from gevent.socket import SOCK_STREAM
from gevent.socket import SOL_SOCKET
from gevent.socket import SO_REUSEADDR
from gevent.socket import SO_KEEPALIVE
from gevent.socket import SHUT_WR
from gevent.socket import IPPROTO_TCP
from gevent.socket import TCP_KEEPIDLE
from gevent.socket import TCP_KEEPINTVL
from gevent.socket import TCP_KEEPCNT
from gevent.socket import gethostbyname
from gevent.socket import gethostbyname_ex
from gevent.socket import error as socket_error

from gevent.ssl import wrap_socket

from gevent.queue import Empty
from gevent.queue import Full

from gevent.select import select

from gevent.greenlet import Greenlet
