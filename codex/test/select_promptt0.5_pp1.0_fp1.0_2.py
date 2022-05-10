import select
# Test select.select()
def test_select():
    # Create two sockets
    s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Bind them to the port
    s1.bind(('localhost', 50007))
    s2.bind(('localhost', 50008))
    # Listen for incoming connections
    s1.listen(1)
    s2.listen(1)
    # Connect to the sockets
    s1.accept()
    s2.accept()
    # Create the three lists of sockets to pass to select.select()
    rlist = [s1, s2]
    wlist = [s1, s2]
    xlist = [s1, s2]
    # Invoke select.select()
    readable, writable, exceptional = select.select(rlist, wlist, xlist)
    # Print the results
    print('readable =', readable)
    print('writable =', writable)
    print
