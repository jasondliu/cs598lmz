import socket
socket.if_indextoname(id)

```


```python
import socket
socket.if_nametoindex("en0")

```


```python
import socket
socket.gethostbyname("www.python.org")

```


```python
import socket
socket.getaddrinfo('www.python.org', 80)

```


```python
import socket
socket.getaddrinfo('www.python.org', 80, socket.AF_INET, socket.SOCK_STREAM, 0, socket.AI_CANONNAME)

```


```python
import socket
socket.gethostbyname_ex('www.python.org')

```


```python
import socket
socket.gethostbyaddr('93.184.216.34')

```


```python
import socket
socket.getnameinfo(('93.184.216.34', 80), socket.NI_NUMERICHOST | socket.NI_NUMERICSERV)

```


```python
import socket
socket.getnameinfo(
