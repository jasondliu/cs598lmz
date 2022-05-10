import sys, threading

def run():
    while True:
        print('thread running')
        time.sleep(1)

def main():
    t = threading.Thread(target=run)
    t.setDaemon(True)
    t.start()

    print('main thread')
    time.sleep(3)
    print('done')

if __name__ == '__main__':
    main()

# 当主线程退出的时候，子线程kill掉
# 如果子线程不kill掉，会成为僵尸进程
