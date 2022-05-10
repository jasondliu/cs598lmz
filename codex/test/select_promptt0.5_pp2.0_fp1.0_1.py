import select
# Test select.select()

# select.select() takes three lists of sockets as arguments, and returns a list of sockets that are ready for reading, writing, or an error.

# For example, to wait for a socket to be ready for reading, use the following code:

# import socket
# import select
# 
# s = socket.socket()
# 
# # set up the socket for listening
# s.bind((host, port))
# s.listen(backlog)
# 
# input = [s]
# 
# running = 1
# while running:
#     inputready, outputready, exceptready = select.select(input, [], [])
# 
#     for s in inputready:
# 
#         if s == server:
#             # handle the server socket
#             client, address = server.accept()
#             input.append(client)
# 
#         elif s == sys.stdin:
#             # handle standard input
#             junk = sys.stdin.readline()
#             running = 0
# 
#         else:
#
