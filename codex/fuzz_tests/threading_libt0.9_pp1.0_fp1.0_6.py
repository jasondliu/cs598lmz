import threading
threading.current_thread()

print(threading.active_count())
print(threading.enumerate())
print(threading.current_thread())

from queue import Queue
from threading import Thread

from time import sleep


def func1(queue):
    """
    模拟一个生成器
    :param queue:
    :return:
    """
    for i in range(5):
        print("produce 1")
        queue.put(i)


def func2(queue):
    """
    从队列拿数据
    :param queue:
    :return:
    """
    while True:
        print("========")
        sleep(2)
        if not queue.empty():
            item = queue.get()
            print(item)
            print("consume {}".format(item))
        else:
            print("queue is empty!")
            break


if __name__ == "__main__":
    # main()
    queue = Queue
