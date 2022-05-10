import socket
socket.if_indextoname(3)

# 查看当前网络接口
socket.if_nameindex()

# 查看当前网络接口
socket.gethostname()

# 查看当前网络接口
socket.gethostbyname(socket.gethostname())

# 查看当前网络接口
socket.gethostbyname_ex(socket.gethostname())

# 查看当前网络接口
socket.gethostbyaddr('8.8.8.8')
