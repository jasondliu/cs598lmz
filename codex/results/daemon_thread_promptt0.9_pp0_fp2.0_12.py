import threading
# Test threading daemon
def run(num):
    print(num)

if __name__ == '__main__':
    for i in range(5):
        t = threading.Thread(target = run, args = (i,))
        t.setDaemon(True)
        t.start()
    print('main thread')
#!! 子线程 必须在父线程之前设置为守护线程 , 并且这个子线程必须死后字线程死亡, 不然会无法结束

# Threading Event
import threading
import time


def run(n):

    while n > 0:
        print(n)
        n -= 1
        time.sleep(1)

if __name__ == '__main__':
    e = threading.Event() # 定义事
