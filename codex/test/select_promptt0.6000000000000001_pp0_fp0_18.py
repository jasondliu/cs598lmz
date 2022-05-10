import select
# Test select.select function

# This function is not really necessary
# all we want is to get the current time
def get_current_time():
    # Get current time
    return time.strftime("%d/%m/%Y %H:%M:%S", time.gmtime())

# Function that waits for a connection
# and returns a tuple of two elements
# the first is the connection
# the second is the address
def accept_connection(server_socket):
    try:
        # Accept the connection
        client_socket, address = server_socket.accept()
        # Return the connection
        return (client_socket, address)
    except IOError as error:
        # If there is an error
        # (maybe a signal)
        # we return None
        return (None, None)

# Function that waits for data to arrive
# and returns a tuple of two elements
# the first is the connection
# the second is the data
