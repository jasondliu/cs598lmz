import socket
socket.if_indextoname('1')

```


```python
# Get ip address
socket.gethostbyname('www.google.com')

```




    '172.217.166.174'




```python
# Get ip address
socket.gethostbyname('www.facebook.com')

```




    '31.13.77.36'




```python
# Get ip address
socket.gethostbyname('www.apple.com')

```




    '17.172.224.47'




```python
# Get ip address
socket.gethostbyname('www.python.org')

```




    '151.101.200.224'



## HOW TO CREATE SOCKET

- socket.socket(socket_family, socket_type, protocol=0)
- socket_family: This is either AF_UNIX or AF_INET, as explained earlier.
- socket_type: This is either SOCK_STREAM or SOCK_DGRAM.
- protocol: This is usually
