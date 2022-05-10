import select
# Test select.select() to do a time out and check if there is data to be read
# todo get this working
# def client():
#
#     # create a TCP/IP socket
#     sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     # then connect to the server
#     server_address = ('192.168.1.78', 7759)
#     sock.connect(server_address)
#
#     for i in range(1, 100):
#         try:
#             # Send data
#             message = 'This is the message.  It will be repeated.'
#             print >>sys.stderr, 'sending "%s"' % message
#             sock.sendall(message)
#             time.sleep(1)
#
#             # Look for the response
#             amount_received = 0
#             amount_expected = len(message)
#             while amount_received < amount_expected:
#                 # data = sock.recv(16)
#                 data = ''
#                 while data == '':
#                     readable,
