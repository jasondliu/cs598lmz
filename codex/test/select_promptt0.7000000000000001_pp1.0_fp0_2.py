import select
# Test select.select

# 下面是模拟客户端请求
# 首先，创建套接字
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 连接到服务器
s.connect(('127.0.0.1', 6666))

# 因为这里是select实现的异步请求，所以必须把套接字设置为非阻塞
s.setblocking(False)

# 这里的第一个参数是要监听的IO，第二个是等待读取的IO，
# 因为这里是客户端
