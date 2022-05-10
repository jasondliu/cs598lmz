import socket
# Test socket.if_indextoname()

def main():
    try:
        indextoname = socket.if_indextoname
    except AttributeError:
        print "socket.if_indextoname not found"
    else:
        print "socket.if_indextoname found"
        ifname = indextoname(1)
        print "interface 1 =", ifname
        try:
            ifname = indextoname(-1)
        except socket.error:
            print "socket.error raised correctly"
        else:
            print "socket.error NOT raised correctly"

if __name__ == "__main__":
    main()
