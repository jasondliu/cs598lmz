import select
# Test select.select() used in tcp_client.py and tcp_server.py
#
#

# Create two sockets
s1 = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s2 = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# Create a list of sockets
sock_list = [s1, s2]

# Create a list of empty lists
rlist, wlist, xlist = [], [], []

# Add the sockets to the empty lists
rlist.append(s1)
rlist.append(s2)

# Test select.select()
rlist, wlist, xlist = select.select(rlist, wlist, xlist, 0)
print(rlist)
print(wlist)
print(xlist)

# Close the sockets
s1.close()
s2.close()
