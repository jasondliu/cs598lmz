import select
# Test select.select() for the ability to do a non-blocking
# connect() within a select() call.  If this works, it should complete
# without delay.  If it hangs, it's a confirmation that the platform
# *doesn't* support a non-blocking connect().

PORT = 50007
HOST = 'localhost'

def find_available_port(host, port, timeout=0.1):
    import socket
    s = socket.socket()
    s.settimeout(timeout)
    while True:
        try:
            s.bind((host, port))
        except socket.error:
            port += 1
        else:
            s.close()
            return port

def blocking_connect(host, port):
    import socket
    s = socket.socket()
    s.connect((host, port))

# find a port that is not being used
port = find_available_port(HOST, PORT)

# execute a blocking connection in a separate process.
# We expect it to finish quickly.
