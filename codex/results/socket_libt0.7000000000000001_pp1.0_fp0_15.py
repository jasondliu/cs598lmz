import socket, sys, threading

# 获取本机主机名
myname = socket.getfqdn(socket.gethostname(  ))
# 获取本机ip
myaddr = socket.gethostbyname(myname)

# 创建 socket 对象
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

# 获取本地主机名
host = '127.0.0.1'
port = 12345

# 绑定端口
serversocket.bind((host, port))

# 设置最大连接数，超过后排队
serversocket.listen(5)

print ('服务器%s正在监听端口%s' %(myaddr,port))
while True:
    #
