import socket
socket.if_indextoname(1)

# 获取接口的索引
socket.if_nametoindex('lo')

# 获取网络地址
socket.gethostbyname('www.baidu.com')
socket.gethostbyname_ex('www.baidu.com')
socket.gethostbyaddr('www.baidu.com')

# socket.gethostname()
# socket.gethostbyname(socket.gethostname())

socket.setdefaulttimeout(1)
socket.gethostbyname('www.baidu.com')

# 获取本机接口
socket.gethostname()
socket.gethostbyname(socket.gethostname())
