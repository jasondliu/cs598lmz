import select
# Test select.select()
import socket

def main():
    # Create a TCP/IP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setblocking(0)
    
    # Bind the socket to the port
    server_address = ('localhost', 10000)
    server_socket.bind(server_address)

    # Listen for incoming connections
    server_socket.listen(5)

    # Sockets from which we expect to read
    inputs = [ server_socket ]
    
    # Sockets to which we expect to write
    outputs = [ ]
    timeout = 20

    # Outgoing message queues (socket:Queue)
    message_queues = {}

    while inputs:
        # Wait for at least one of the sockets to be ready for processing
        print >>sys.stderr, '\nwaiting for the next event'
        readable, writable, exceptional = select.select(inputs, outputs, inputs, timeout)

        # Handle inputs
