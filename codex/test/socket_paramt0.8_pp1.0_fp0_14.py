import socket
socket.if_indextoname(2)

#2. 获取名称对应的索引项
socket.if_nameindex()

#3. 获取当前主机名称
socket.gethostname()

#4. 获取主机的ip地址
socket.gethostbyname_ex('www.baidu.com')[2][0]
# 参数: 1:HTTP 1.0(80)   2: HTTP 1.1(443)
socket.gethostbyname_ex('www.baidu.com')[2][1]

#5. 获取所有的接口信息
socket.if_nameindex()

#6. 获取所有的接口名称
socket.if_nameindex()

#7. 格式化所有的接口信息
