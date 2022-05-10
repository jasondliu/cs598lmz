import socket
# Test socket.if_indextoname()
 
def test(family, addr, flags, if_name):
    af_map = {socket.AF_INET: 'AF_INET',
              socket.AF_INET6: 'AF_INET6'}
 
    try:
        result = socket.if_indextoname(if_name)
    except OSError as err:
        print("socket.if_indextoname({}) failed: {}".format(if_name, err))
        return
 
    print("socket.if_indextoname({}) = {}".format(if_name, result))
 
 
test(socket.AF_INET, '127.0.0.1', socket.AI_DEFAULT, 1)
</code>

