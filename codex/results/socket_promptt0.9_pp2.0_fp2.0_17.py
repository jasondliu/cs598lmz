import socket
# Test socket.if_indextoname()
print(socket.if_indextoname(5))
```

```
root@5c6f360f3684:~# python3 netsocket.py
eth0
```

## socket.if_nameindex()

**socket.if_nameindex()** - Return an array of tuples containing interface index and interface name

```
print(socket.if_nameindex())
```

```
root@5c6f360f3684:~# python3 netsocket.py
[(1, 'lo'), (2, 'eth0')]
```

## socket.getdefaulttimeout()

**socket.getdefaulttimeout()** - Return the default timeout value

```
print(socket.getdefaulttimeout())
```

```
root@5c6f360f3684:~# python3 netsocket.py
None
```

## socket.gethostbyname_ex(hostname)

**socket.gethostbyname_ex(hostname)** - Return the hostname, a list of alternative hostname
