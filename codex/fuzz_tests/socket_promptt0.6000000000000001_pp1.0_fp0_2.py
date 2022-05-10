import socket
# Test socket.if_indextoname()
def test(indx):
    try:
        print("%s => %s" % (indx, socket.if_indextoname(indx)))
    except Exception as e:
        print("%s => %s" % (indx, e))

print("Test basic usage")
test(-1)
test(0)
test(1)
test(1024)

print("Test invalid index")
test(-2)
test(-1024)
test(-1025)
test(-10000)

print("Test index out of range")
test(1023)
test(1025)
test(9999)
test(10000)

try:
    socket.if_indextoname(None)
except TypeError:
    print("Cannot pass None as argument")
