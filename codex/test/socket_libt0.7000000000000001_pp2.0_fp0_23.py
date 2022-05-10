import socket
import time

from pymouse import PyMouse
from pykeyboard import PyKeyboard



def controlMouse():
    m = PyMouse()
    k = PyKeyboard()
    sock=socket.socket()
    sock.connect(("192.168.1.100",8888))
    while True:
        data=sock.recv(1024)
        print (data)
        if data==b'1':
            m.move(10, 0)
        elif data==b'2':
            m.move(-10, 0)
        elif data==b'3':
            m.move(0, 10)
        elif data==b'4':
            m.move(0, -10)
        elif data==b'5':
            m.click(m.position()[0],m.position()[1])
        elif data==b'6':
            k.tap_key(k.space)
        elif data==b'7':
            k.tap_key(k.left_key)
