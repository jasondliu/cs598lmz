import socket
# Test socket.if_indextoname
socket.if_indextoname(0x1)

import _socket
# Test _socket.if_indextoname
_socket.if_indextoname(0x1)

import nis
# Test nis.cat
nis.cat('passwd.byname')

import _nis
# Test _nis.cat
_nis.cat('passwd.byname')

import _ssl
# Test _ssl.enum_certificates
_ssl.enum_certificates('CA')

import termios
# Test termios.tcgetattr
termios.tcgetattr(0)

import _termios
# Test _termios.tcgetattr
_termios.tcgetattr(0)

import _curses
# Test _curses.tparm
_curses.tparm(1)

import _curses_panel
# Test _curses_panel.bottom_panel
_curses_panel.bottom_panel(0)

import _multibytecodec
# Test _multibytecodec.__getcodec
