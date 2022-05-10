import threading
# Test threading daemon
socket_list = []
connect_list = []
def Thread(sock):
    global socket_list, connect_list
    while True:
        # Listen
        if sock in select.select([sock],[], [], 0)[0]:
            # New connection
            con_sock, addr = sock.accept()
            # Store new connection
            socket_list.append(con_sock)
            connect_list.append(addr)
            print("New connection from:{}".format(addr))
        # Check connection
        for s in socket_list:
            if s in select.select([s],[], [], 0)[0]:
                try:
                    data = s.recv(1024)
                    if data:
                        print("Received:{} from:{}".format(data, connect_list.index(s.getpeername())+1))
                    else:
                        socket_list.remove(s)
                        connect_list.remove(s.getpeername())
                        s.close()
                        print("Connection from:{} is closed.".format(s.getpeername()))
