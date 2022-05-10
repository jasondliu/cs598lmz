import socket
# Test socket.if_indextoname
def socket_if_indextoname_test():
    index = 2
    name = socket.if_indextoname(index)
    print "the index of name is %s" % str(name)

def socket_if_indextoname_test2():
    print "The number of complete."
if __name__ == '__main__':
    try:
        socket_if_indextoname_test()
    except:
        print "Error,there is no the index in your system."
    else:
        socket_if_indextoname_test2()
