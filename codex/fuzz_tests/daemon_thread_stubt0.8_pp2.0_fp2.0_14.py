import sys, threading

def run():
    print(threading.current_thread().getName())
    for i in range(1000):
        print(i)

if __name__ == '__main__':
    # 构造新的线程
    t1 = threading.Thread(target=run)
    t2 = threading.Thread(target=run)

    # 启动新线程
    t1.start()
    t2.start()

    t1.join()
    t2.join()
    # 检查线程是否活动
    print(t1.is_alive())
    print(t2.is_alive())
    print(threading.current_thread().getName())
