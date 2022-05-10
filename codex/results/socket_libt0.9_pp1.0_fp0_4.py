import socket通过各种方式建立连接，使用连接对象，调用send与recv等方法来发送与接收数据，当需要结束连接的时候，使用close方法来进行关闭。
#UDP的使用顺序可以分解成三部分：
#首先，创建sockaddr_in结构，填充必须的参数，包括AF_INET（使用IPv4），对方的IP地址与端口号，自己的端
