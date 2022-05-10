import socket
socket.if_indextoname(2)
```

## Docker

```bash
docker run --rm -p 5000:5000 -v $(pwd):/host -v /etc:/host/etc -v /usr/local/etc:/host/usr/local/etc --net=host pwn:latest
```
