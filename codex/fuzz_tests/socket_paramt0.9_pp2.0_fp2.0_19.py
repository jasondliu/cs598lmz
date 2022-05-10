import socket
socket.if_indextoname(2)

#print the name of the network interface
    
    
    
    

print "name of network interface ",socket.if_nameindex()
print "name of network interface with index 2",socket.if_indextoname(2)


# no means no of of options


optname,level,opttype,optlen,optval=socket.getaddrinfo('210.210.14.108',0,0,0,0)
print optname
print level
print opttype
print optlen
print optval


# no options
socket.getaddrinfo('210.210.14.108',0,0,0,0)
def disp(optval):
    for i in optval:
        print optval[i]
disp(optval)
def getoptname(optname):
    for i in optname:
        print optname[i]
getoptname(optname)

# find protocol name
print socket.getdefaulttimeout()
print socket.getservbyname('www')
print socket.getservbyport(80)
print socket.
