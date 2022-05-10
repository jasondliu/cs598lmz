import socket
# Test socket.if_indextoname()

def test(family, address):
    try:
        print(socket.if_indextoname(family, address))
    except OSError as e:
        print(e)

print('AF_INET:')
test(socket.AF_INET, b'\x00\x00\x00\x00')
test(socket.AF_INET, b'\x00\x00\x00\x01')
test(socket.AF_INET, b'\x00\x00\x00\x02')
test(socket.AF_INET, b'\x00\x00\x00\x03')
test(socket.AF_INET, b'\x00\x00\x00\x04')
test(socket.AF_INET, b'\x00\x00\x00\x05')
test(socket.AF_INET, b'\x00\x00\x00\x06')
