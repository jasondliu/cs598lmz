import socket
socket.if_indextoname(3)

# Output: 'en0'

```

```python

import socket
socket.if_nametoindex('en0')

# Output: 3

```

```python

import socket
socket.getaddrinfo('www.baidu.com', 'http')

# Output: [(2, 1, 6, '', ('123.125.114.144', 80)), (2, 2, 17, '', ('123.125.114.144', 80)), (2, 3, 0, '', ('123.125.114.144', 80))]

```

```python

import socket
socket.gethostbyname('www.baidu.com')

# Output: '123.125.114.144'

```

```python

import socket
socket.gethostbyname_ex('www.baidu.com')

# Output: ('www.a.shifen.com', [], ['123.125.114.144'])

```

```python

import socket

