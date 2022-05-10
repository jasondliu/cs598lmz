import select
import socket
import sys
import threading
import time

import pytest

import curio
from curio import socket as csock
from curio.socket import *
from curio.socket import _socket
from curio.socket import _socketpair
from curio.socket import _socketpair_linux
from curio.socket import _socketpair_osx
from curio.socket import _socketpair_windows
from curio.socket import _socketpair_freebsd
from curio.socket import _socketpair_openbsd
from curio.socket import _socketpair_netbsd
from curio.socket import _socketpair_dragonfly
from curio.socket import _socketpair_solaris
from curio.socket import _socketpair_aix
from curio.socket import _socketpair_hpux
from curio.socket import _socketpair_irix
from curio.socket import _socketpair_android
from curio.socket import _socketpair_cygwin
from curio.socket import _socketpair_haiku
from curio.socket import _socketpair_sun
