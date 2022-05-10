import select
# Test select.select
# fd_event_list_1 = select.select([sys.stdin], [], [], 1.0)
# print("======= fd_event_list_1: {0}".format(fd_event_list_1))

# import socket
# # Create a TCP socket
# sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# print("======= sock: {0}".format(sock))
# # Set socket to nonblocking mode
# sock.setblocking(0)
# # Bind socket to port 5050 and any interface
# sock.bind(("", 5050))
# # Start listening
# sock.listen(5)
# # Test select.select
# fd_event_list_2 = select.select([sock], [], [], 1.0)
# print("======= fd_event_list_2: {0}".format(fd_event_list_2))
# # Test select.select
# fd_event_list_3 = select.select([sock], [], [],
