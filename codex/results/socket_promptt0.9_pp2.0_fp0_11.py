import socket
# Test socket.if_indextoname
def test(args = None):
    
    

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    msg = b'dummy'
    addr = ('localhost', 9999)
    s.sendto(msg, addr)

    if len(args) > 1:
        index = int(args[1])
    else:
        index = pysockets_lib.getifindex()

    try:
        print(index, '->', socket.if_indextoname(index))
    except ValueError:
        if sys.platform == "darwin":
            # Darwin only accepts native if_index
            raise

    
    



if __name__ == "__main__":
    test(sys.argv)
