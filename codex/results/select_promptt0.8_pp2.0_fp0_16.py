import select
# Test select.select()

# List of sockets to watch. 
# Each socket is identified with a numerical file descriptor
# select will monitor this list of file descriptors

sockets = []


#===================
#===================
def create_socket():
    ''' Create a socket, when the socket has been created the socket_created()
    method is called

    '''
    global server_socket

    # Create a TCP/IP socket
    server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server_socket.setblocking(0)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # Bind the socket to the port and interface
    server_address = ('127.0.0.1', 8081)
    print ("Starting up on {} port {}".format(*server_address))
    server_socket.bind(server_address)

    # Listen for incoming connections
    server_socket.listen(5)

    # Add the listener socket to the list of sockets to monitor
   
