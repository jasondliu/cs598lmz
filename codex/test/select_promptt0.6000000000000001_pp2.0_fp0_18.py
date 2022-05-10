import select
# Test select.select()
# 创建两个socket对象
s1 = socket.socket()
s2 = socket.socket()
# 设置为非阻塞模式
s1.setblocking(False)
s2.setblocking(False)
# 准备好了,可以接收连接
s1.bind(('localhost', 8001))
s1.listen(10)
# 客户端准备连接
s2.connect(('localhost', 8001))
# 创建一个列表,把两个socket对象放在里面
ls = [s1, s2]
# 循环
