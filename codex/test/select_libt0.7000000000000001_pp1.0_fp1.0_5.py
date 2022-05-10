import selectors
import socket
import queue
import time
import os
import time

sel = selectors.DefaultSelector()


def select_to_queue(fileobj, mask, q):
    # 数据可读
    # 把数据放入队列
    q.put(fileobj.recv(1000))
    # 关闭文件
    fileobj.close()


def accept(sock, mask):
    conn, addr = sock.accept()  # Should be ready
    print('accepted', conn, 'from', addr)
    # 把数据放入队列
    q = queue.Queue()
    # 创建描述符并设置为可读
    sel.register(conn, selectors.EVENT_READ, select_to_queue(conn, mask, q))
    # 从队列中获取
