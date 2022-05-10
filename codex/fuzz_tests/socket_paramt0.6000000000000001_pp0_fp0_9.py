import socket
socket.if_indextoname(3)

# 如果没有找到相应的网络接口，将返回ValueError异常
socket.if_indextoname(1000)

# 查找网络接口的索引，可以使用if_nameindex()方法
socket.if_nameindex()

# 要想获得网络接口的状态，可以使用if_nametoindex()
socket.if_nametoindex('en0')

# 要想获得网络接口的地址，可以使用if_nameindex()方法
socket.if_nametoindex('en0')

# 获取网络接口的地
