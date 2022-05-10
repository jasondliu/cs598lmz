import lzma
lzma.open

# test imp format (file_magic, ext, etc)
# todo: add log.info
import imp
imp.get_magic

# test importlib / importlib.abc
import importlib
importlib.util

# test sqlite3
import sqlite3
sqlite3.register_adapter()

# test typing
import typing

# test http.client
import http.client
http.client.HTTPConnection.connect

# test _dummy_thread
import _dummy_thread
_dummy_thread.get_ident()

# test zipfile
import zipfile
zipfile.ZipFile(mode='w', compression=zipfile.ZIP_BZIP2)

# test urllib.request
import urllib.request
urllib.request.urlopen()

# test socketserver
import socketserver
socketserver.TCPServer(server_address=('192.168.0.1', 80), RequestHandlerClass=socketserver.BaseRequestHandler)

# test email
import email
email.message_from_
