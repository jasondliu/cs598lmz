import select
# Test select.select()

def poll_for_data(sock):
    # Wait for at most 5 seconds
    timeout = 5
    # Block at most until there is data to read
    rlist, wlist, xlist = select.select([sock], [], [], timeout)
    if rlist:
        data = sock.recv(1024)
        return data
    else:
        return None

# Test select.poll()

def poll_for_data(sock):
    # Wait for at most 5 seconds
    timeout = 5000
    poll_object = select.poll()
    poll_object.register(sock, select.POLLIN)
    # Block at most until there is data to read
    ready = poll_object.poll(timeout)
    if ready:
        data = sock.recv(1024)
        return data
    else:
        return None

# Test select.epoll()

def poll_for_data(sock):
    # Wait for at most 5 seconds
    timeout = 5
    epoll = select.epoll()
