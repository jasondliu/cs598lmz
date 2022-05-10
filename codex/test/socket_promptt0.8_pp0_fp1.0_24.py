import socket
# Test socket.if_indextoname()
for i in range(1,100):
    try:
        name = socket.if_indextoname(i)
    except:
        pass
    else:
        print(i,name)
