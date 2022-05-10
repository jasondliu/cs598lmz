import select
# Test select.select()

read_list=[server]
write_list=[]
error_list=[server]
timeout=10

readable, writeable, errored = select.select(read_list, write_list, error_list, timeout)

for s in readable:
    if s is server:
        # A "readable" socket is ready to accept a connection
        connection, client_address = s.accept()
        print("New connection from {}".format(client_address))
    else:
        data = s.recv(1024)
        if data:
            # A readable client socket has data
            print("Received {!r}".format(data))
            s.sendall(data)
        else:
            print("Closing {}".format(client_address))
            s.close()
</code>
I don't know what else to try.
I have tried the code on my laptop and it works fine.

