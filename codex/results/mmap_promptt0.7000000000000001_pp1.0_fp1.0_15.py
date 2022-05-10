import mmap
# Test mmap.mmap(0, 10, 'MAP_PRIVATE').move(0, 0, 0)

import quopri
# Test quopri.encodestring(b'hello')

import readline
# Test readline.get_completer_delims()

import resource
# Test resource.getrlimit(resource.RLIMIT_STACK)

import select
# Test select.poll().poll()

import socket
# Test socket.socket().getsockname()

import ssl
# Test ssl.wrap_socket(socket.socket(), cert_reqs=ssl.CERT_NONE)

import sys
# Test sys.getrecursionlimit()

import termios
# Test termios.tcgetattr(0)

import textwrap
# Test textwrap.TextWrapper().wrap('')

import timeit
# Test timeit.default_timer()

import tkinter
# Test tkinter.Tk()

import wave
# Test wave.open('pystone.wav', 'rb').getnframes()

import xml.etree
