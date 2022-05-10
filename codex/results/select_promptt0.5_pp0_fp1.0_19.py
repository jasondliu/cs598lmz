import select
# Test select.select()
#
#

#
# This function is called when a new connection is made to the server.
#
def handle_connection( connection, address ):
    print "New connection from", address
    connection.send("Welcome to the server\n")
    while True:
        data = connection.recv( 1024 )
        if not data:
            break
        connection.send( data )
    connection.close()


#
# This is the main server loop.  It creates a new socket and binds it to
# the port given on the command line.  Then it listens for incoming
# connections.  When one is detected, handle_connection() is called
# to deal with the new socket.
#
def main( port ):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(('', port))
    s.listen(5)
    print "Listening on port", port
    while True:
       
