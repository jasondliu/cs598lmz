import socket
socket.if_indextoname(7)

# socket.error should be a FunctionType
import socket
isinstance(socket.error, types.FunctionType)

# socket.error returns socket.error instance
import socket
socket.error()

# socket.timeout should be a type object
import socket
isinstance(socket.timeout, types.TypeType)

# socket.timeout is a subclass of socket.error
import socket
issubclass(socket.timeout, socket.error)

# socket.timeout('') should return socket.timeout instance
import socket
socket.timeout('')

# socket.herror should be a type object
import socket
isinstance(socket.herror, types.TypeType)

# socket.herror is a subclass of socket.error
import socket
issubclass(socket.herror, socket.error)

# socket.herror('') should return socket.herror instance
import socket
socket.herror('')

# socket.gaierror should be a type object
import socket
isinstance(socket.gaierror, types.TypeType)

# socket.gaier
