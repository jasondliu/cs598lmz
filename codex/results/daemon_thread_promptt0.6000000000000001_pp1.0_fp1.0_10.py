import threading
# Test threading daemon

def thread_func(name):
    print('start threading')
    for i in range(3):
        time.sleep(1)
        print('%s is running' % name)
    print('%s is done' % name)


def main():
    t = threading.Thread(target=thread_func, args=('dazuo',))
    t.setDaemon(True)
    t.start()

    for i in range(3):
        time.sleep(1)
        print('main is running')
    print('main is done')

if __name__ == '__main__':
    main()

# 一个线程需要的时间远大于主线程，所以没有等待子线程执行完成，主线程就结束了
# 这时候把子线
