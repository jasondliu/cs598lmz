import select
# Test select.select
'''
print('Select Start')
rs, ws, es = select.select([self], [self], [self])
for sock in rs:
    if sock is self: # 监听套接字
        # 收到监听套接字的通知，表示有客户端连接
        client_sock, client_addr = self.accept()
        print(client_addr, "连入服务器")
        client_sock.recv(1024)
        client_sock.close()
    else: # 客户端套接字
        print(sock, "发来数据")
print('Select End')
'''

import queue

# 阻塞队列
q = queue.Queue()
q.get()
q.put(1)
q.put(2)
# print(q.get
