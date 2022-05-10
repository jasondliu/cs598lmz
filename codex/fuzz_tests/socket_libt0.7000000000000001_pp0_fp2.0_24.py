import socket
+import threading
+
+
+# 定义常量，即本机IP和端口号
+IP_ADDRESS = '127.0.0.1'
+PORT_NUMBER = 8800
+
+# 创建一个socket对象
+s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
+# 将套接字绑定到地址，这里IP:PORT为本机IP和端口号
+s.bind((IP_ADDRESS, PORT_NUMBER))
+
+
+# 将套接字设置为被动监听模式，等待连接的到来
+s.listen(1)
+
+print('Server is running...')
