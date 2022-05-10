import select
import socket
import sys
import threading
import time

import pytest

import curio
from curio import socket as csock
from curio import ssl as cssl
from curio.socket import *
from curio.ssl import *
from curio.traps import _read_wait, _write_wait
from curio.traps import _sock_recv_into, _sock_send_all
from curio.traps import _sock_recv_some, _sock_send_some
from curio.traps import _sock_accept, _sock_connect
from curio.traps import _sock_connect_ex, _sock_recvfrom_into
from curio.traps import _sock_sendto_all, _sock_recvfrom_some
from curio.traps import _sock_sendto_some, _sock_recvmsg_into
from curio.traps import _sock_sendmsg_all, _sock_recvmsg_some
from curio.traps import _s
