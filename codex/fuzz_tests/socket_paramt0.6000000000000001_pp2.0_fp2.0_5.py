import socket
socket.if_indextoname(3)

socket.gethostbyname('www.baidu.com')

# 获取域名对应的IP地址，可以设置超时时间
import socket
socket.gethostbyname_ex('www.baidu.com')
# 域名的解析，结果是一个元组，第一个元素是域名，第二个元素是域名的别名，第三个元素是域名对应的IP地址

# 获取域名对应的IP地址
import socket
socket.gethostbyname_ex('www.baidu.com')[2]

# 获取域名
