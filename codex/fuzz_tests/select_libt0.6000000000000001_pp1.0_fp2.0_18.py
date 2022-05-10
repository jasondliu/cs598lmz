import select

# 创建监听套接字
sockfd = socket()
sockfd.bind(('0.0.0.0',8888))
sockfd.listen(5)

# 设置为非阻塞
sockfd.setblocking(False)

# 创建poll对象
p = select.poll()

# 创建查找字典
fdmap = {sockfd.fileno():sockfd}

# 注册关注IO
p.register(sockfd,select.POLLIN | select.POLLERR)

# 循环监控IO发生
while True:
    # 返回值是IO的列表[(fileno,event),(),()]
    events = p.poll()
    # 遍历列表,处理IO
   
