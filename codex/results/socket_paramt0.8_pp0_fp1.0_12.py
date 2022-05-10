import socket
socket.if_indextoname(2)
#网卡的识别码是2，因此返回了‘eth1:’ ，
socket.if_nameindex()
#返回了[(1, 'lo'), (2, 'eth1')] 。
'''

# 3.2 获取本机IP地址
'''
我们使用ip地址与主机名交互，所以我们需要先获取到本机的ip地址。
下面是获取本机IP地址的示例：
import socket
socket.gethostbyname(socket.gethostname())
#返回了'192.168.2.107' 。
'''

# 3.3 套接字
'''
套
