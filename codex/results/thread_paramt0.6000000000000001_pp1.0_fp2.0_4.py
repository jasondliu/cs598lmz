import sys, threading
threading.Thread(target=lambda:sock.listen(1)).start()
while True:
    conn, addr = sock.accept()
    from_client = ''
    while True:
        data = conn.recv(4096)
        if not data: break
        from_client += data
        print(from_client)
    conn.close()
    print('client disconnected')
</code>
I have also tried using <code>sock.setblocking(0)</code> but that didn't help.
I'm using Python 3.3.2 on Windows 7.


A:

The problem is that your main thread is busy waiting for the client to connect.  The <code>accept</code> call blocks until a connection is established.  Once the connection is established, the main thread will process the connection, which means that it will not be able to process any other connections until it has processed the first one.  This is why you get the "pipe broken" error.
To fix this, you can use a thread to handle connections.  For example:
<code>import socket, sys, threading

def handle_connection(conn, addr):

