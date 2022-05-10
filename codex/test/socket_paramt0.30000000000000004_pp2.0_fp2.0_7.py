import socket
socket.if_indextoname(2)

# 使用socket.if_nameindex()函数获取所有网络接口的索引号和名称
socket.if_nameindex()

# 使用socket.gethostbyname()函数获取域名的IP地址
socket.gethostbyname('www.baidu.com')

# 使用socket.gethostbyname_ex()函数获取域名的IP地址、主机名和别名
socket.gethostbyname_ex('www.baidu.com')

# 使用socket.gethostname()函数获取本机主机名
socket.gethostname()

# 使用socket.gethostbyaddr()函数获取IP地址的主
