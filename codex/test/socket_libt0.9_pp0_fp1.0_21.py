import socket
import threading
import urllib
hello = 'hello'
header = 'HTTP/1.1 200 OK\r\ncontent-type: text/html\r\n'
header += 'content-length: %d\r\n\r\n' % len(hello)

