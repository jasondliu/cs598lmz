import socket
socket.if_indextoname(3)

#If there is no physical interface with the given index, OSError is raised.

#If the index is out of range, ValueError is raised.

#Changed in version 3.3: Indexes are now returned as int.

print()

# 19.6.2.6.1.6 socket.if_nametoindex(ifname)¶

#Return the index of the network interface named ifname.

socket.if_nametoindex('lo')

#If the interface does not exist, OSError is raised.

#Changed in version 3.3: Return value is now int.

print()

# 19.6.2.6.1.7 socket.if_nameindex()¶

#Return a list of network interface information.

#Each entry in the list contains a tuple with the following information:

#if_index
#Index of interface
#if_name
#Name of interface

interfaces = socket.if_nameindex()

print(interfaces)
#[(1, 'lo'), (2, 'enp0
