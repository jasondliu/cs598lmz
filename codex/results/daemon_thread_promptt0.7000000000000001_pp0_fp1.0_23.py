import threading
# Test threading daemon mode
def test_threading_daemon():
    # 创建一个子线程
    t = threading.Thread(target=test_daemon, name='Daemon_Thread')
    # 设置子线程为守护线程
    t.setDaemon(True)
    # 启动子线程
    t.start()
    # 主线程退出
    print("Main thread exit")

def test_daemon():
    while True:
        time.sleep(1)
        print("Daemon thread is running...")



if __name__ == '__main__':
    test_threading_daemon()
