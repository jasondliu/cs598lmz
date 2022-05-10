import socket
socket.if_indextoname('6')

socket.if_indextoname(6)

# socket.if_nameindex() 返回接口到索引号映射的列表。

socket.if_nameindex()

# socket.if_nametoindex(interface) 将接口名称映射到索引号。

socket.if_nametoindex('lo')

# socket.gethostname() 返回当前主机名。

socket.gethostname()

# socket.gethostbyname(hostname) 根据主机名返回对应的IP地址。
socket.gethostbyname('www.baidu.com')

# socket.gethostbyname_ex(hostname) 同上，多返回一个列表，这个列表中包
