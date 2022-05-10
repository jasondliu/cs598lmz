import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
while lst:keepali0e.append(lst[:])
</code>
It produces:
<code>sys:1: ResourceWarning: unclosed &lt;socket.socket object, fd=4, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('[::1]:49783', 0), raddr=('[::1]:8000', 8000)&gt;
</code>
Could I avoid that?
Other question: could be the code improved by reducing the amount of code?
EDIT:
The code for the server:
<code>def x_thread(connection,client_address):
        try:
            print 'connection from', client_address
            # Receive the data in small chunks and retransmit it
            while True:
                data = connection.recv(16)
                print 'received "%s"' % data
                if data:
                    print 'sending data back to the client'
                    connection.sendall(data)
                else:
                    print 'no more data from', client_address
                    break
        finally:
            # Clean up the connection
            connection.close()
