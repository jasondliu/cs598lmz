import select
# Test select.select() using the polling strategy
#
# Explaination: The regular select() call takes a list of sockets and returns
# them. It is the caller who is supposed to send/receive data to/from them.
# The driver specifically uses polling strategy to send/retrieve data from
# all the clients. This is because it is likely that if one client fails,
# others wont and so the driver should collect data from all healthy clients
# to minimize the impact of failure.
#
# NOTE: select.select() is for synchronous programming only -- and not for
# asynchronous programming using threads

client_ports = [9001, 9002, 9003, 9004, 9005, 9006, 9007, 9008, 9009]
client_socks = []
server = ('127.0.0.1', 9000)

# Create sockets at server end
server_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_sock.bind(server)
print('Server created at', server)
server_sock.setblocking(0)
