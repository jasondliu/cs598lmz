import socket
socket.if_indextoname(3)

# 'en0'
```

### gethostbyname

```python
import socket
socket.gethostbyname("www.google.com")

# '216.58.209.206'
```

### gethostbyname_ex

```python
import socket
socket.gethostbyname_ex("www.google.com")

# ('www.google.com', [], ['216.58.209.206'])
```

### gethostbyaddr

```python
import socket
socket.gethostbyaddr("216.58.209.206")

# ('lb-in-f206.1e100.net', [], ['216.58.209.206'])
```

### gethostname

```python
import socket
socket.gethostname()

# 'MacBook-Pro.local'
```

### gethostbyname_ex

```python
import socket
socket.gethostbyname_ex("www.google.com")

# ('www.google.com',
