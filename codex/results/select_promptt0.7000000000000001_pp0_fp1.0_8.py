import select
# Test select.select()

# select.select():
#   input_list = [socket_listen, sys.stdin]
#   output_list = []
#   exception_list = [socket_listen]
#   readable_list, writable_list, exceptional_list = select.select(input_list, output_list, exception_list)
#   if socket_listen in readable_list:
#       # new connection
#       sock, address = socket_listen.accept()
#       input_list.append(sock)
#   elif sys.stdin in readable_list:
#       # stdin
#       cmd = sys.stdin.readline()
#       if cmd == 'quit\n' or cmd == 'exit\n':
#           break;
#   for sock in readable_list:
#       # sockets
#       if sock == socket_listen:
#           continue
#       data = sock.recv(1024)
#       if data:
#           print data
#       else:
#           input_list.remove(sock)
#           sock
