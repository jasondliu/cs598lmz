import socket
socket.if_indextoname(63)
 
socket.socket()
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 
s.bind(('', 80))
 
s.listen()
 
(conn, addr) = s.accept()
 
conn.send(b'''\
HTTP/1.0 200 OK
 
Hello world!
''')
 
conn.close()
```

**Socket:**
connect: connect to a given address
accept: wait for and return the next connection
recv: receive data
send: send data

**Bytes:**
```python
'B'.encode()
'B'.encode('ascii')
'B'.encode('ascii', 'strict');
b'B'
b'xn--'
 
b'B'.decode()
b'B'.decode('ascii')
b'xn--'.decode('idna')
b'B'.decode('ascii', 'strict')
```

**File:**
``
