import socket
# Test socket.if_indextoname()
for i in range(0, 10):
    try:
        print(socket.if_indextoname(i))
    except Exception as e:
        print(e.args[0])
# Test socket.if_nameindex()
for i in socket.if_nameindex():
    print(i)
# Test socket.if_nametoindex()
print(socket.if_nametoindex('lo'))
print(socket.if_nametoindex('eno1'))
print(socket.if_nametoindex('eno2'))
print(socket.if_nametoindex('eno3'))
print(socket.if_nametoindex('eno4'))
# Test socket.gethostbyname_ex()
# print(socket.gethostbyname_ex('localhost'))
# print(socket.gethostbyname_ex('www.python.org'))
# print(socket.gethostbyname_ex('www.baidu.com'))
# print(socket.gethostbyname_ex('www.google.com'))
# Test socket.get
