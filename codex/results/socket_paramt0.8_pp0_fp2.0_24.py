import socket
socket.if_indextoname(3)

#Encontrar la direccion ip del host en linux
hostname = socket.gethostname()
socket.gethostbyname(hostname)

#Conocer la direccion IP sepudieron encontrar
socket.getaddrinfo('google.com', 80)
```

```python
#Establecer un servidor
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("", 8080))
s.listen()

#A la espera de un cliente
client_socket, client_address = s.accept()

#recibir data
data = client_socket.recv(1024)

#Enviar data
client_socket.send("Hola Cliente")
client_socket.close()

s.close()
```

#### Sockets UDP

```python
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(("", 12000))


