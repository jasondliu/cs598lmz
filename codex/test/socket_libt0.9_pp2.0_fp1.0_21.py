import socket

# get socket and the remote end of the connection. The server does not use any new connection-based
# protocol for communication with the client. It just sends the data and closes the connection.
# When connection is closed, the remote end of the connection is disconnected from the server,
# but not from the socket.

# Telling the client that the connection has closed is done by the server sending out a FIN flag.
# When the ACK that indicates that the packet has been received, is sent out, the remote end of the
# connection disappears from the server.

local_port_3 = 5003
socket_3 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_3.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
socket_3.bind(("127.0.0.1", local_port_3))
socket_3.listen(1)  # maximum length of queued connections

client_conn, client_address = socket_3.accept()  # connection established
