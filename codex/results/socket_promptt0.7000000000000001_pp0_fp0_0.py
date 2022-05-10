import socket
# Test socket.if_indextoname(0)
print("Test 0:", socket.if_indextoname(0))
# Test socket.if_indextoname(None)
print("Test None:", socket.if_indextoname(None))
# Test socket.if_indextoname(None, 0)
print("Test None, 0:", socket.if_indextoname(None, 0))
# Test socket.if_indextoname("")
print("Test \"\":", socket.if_indextoname(""))

@micropython.viper
def test_func(a):
    a[:] = [0]

def main():
    src = bytearray(1)
    test_func(src)
    print(src)

main()
