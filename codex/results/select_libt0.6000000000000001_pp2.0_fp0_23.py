import select
import sys

def read_input(fd):
    # read the user input
    return fd.readline()

def process(data):
    # do something here
    return data.upper()

def write_output(fd, data):
    # send back data
    fd.write(data)
    fd.flush()

def main():
    # prepare the server socket
    server = socket.socket()
    server.bind(('0.0.0.0', 9999))
    server.listen(5)

    # prepare the list of sockets to be monitored
    inputs = [server]

    while True:
        # monitor sockets for I/O completion
        readable, writable, exceptional = select.select(inputs, [], [])

        for fd in readable:
            # accept the new connection
            if fd == server:
                client, client_addr = server.accept()
                inputs.append(client)
            # read the user input
            else:
                data = read_input(fd)
                if not data:
                    inputs.
