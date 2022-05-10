import socket
socket.if_indextoname(0)
socket.if_indextoname(1)
```

### Exercise: Use `ifconfig` to get the IP addresses and MAC addresses of your network adapters

```bash
$ ifconfig
```

### Exercise: Use `ping` to send a packet to a host and get a response back

```bash
$ ping www.google.com
```

### Exercise: Use `arp` to view the ARP cache

```bash
$ arp
```

### Exercise: Use `netstat` to view the route table

```bash
$ netstat -r
```

### Exercise: Use `traceroute` to show the route packets take to a host

```bash
$ traceroute www.google.com
```

## References

* https://docs.python.org/3/library/socket.html
* https://docs.python.org/3/library/ipaddress.html
* https://docs.python.org/3/library/struct.html
* http://man7.org/linux/man-pages/man
