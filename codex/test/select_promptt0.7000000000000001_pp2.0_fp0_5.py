import select
# Test select.select
"""
select.select(rlist, wlist, xlist[, timeout])

Wait until one or more file descriptors are ready for some kind of I/O. The
first three arguments are sequences of file descriptors to be waited for: rlist
-- wait until ready for reading, wlist -- wait until ready for writing, xlist --
wait for an ``exceptional condition'' (see the manual page for what your system
considers such a condition).
"""

def testselect():
    import random
    import time
    import socket
    import threading
    # Create a tcp socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('127.0.0.1', 0))
    s.listen(1)
    # Create a thread to accept the connection
    connected = threading.Event()
    def server():
        conn, addr = s.accept()
        connected.set()
        conn.close()
    st = threading.Thread(target=server)
    st.daemon = True
    st.start
