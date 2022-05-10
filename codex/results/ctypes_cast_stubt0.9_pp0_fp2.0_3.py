import ctypes
ctypes.cast(10, ctypes.py_object)

a = 1

ctypes.cast(10, ctypes.py_object) + a

s = ctypes.cast(10, ctypes.py_object) + 10

type(s)

s.value

# s.value + 10


a = 1 + \
    2

a
a = (1 + 
     2)
a

5.5 + 10.5

# without parenthesis
5.5 +
10.5

# with parenthesis
(5.5 +
10.5)

import socket

remote_host = 'www.google.com'
ip = socket.gethostbyname(remote_host)

ip

user = 'aspiring'
passwd = ''

cred = user + ':' + passwd

cred

cred = '{}:{}'.format(user, passwd)

cred

cred = user + ':' + passwd

cred

# new in python3
f'{user}:{passwd
