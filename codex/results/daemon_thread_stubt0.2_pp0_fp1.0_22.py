import sys, threading

def run():
    while True:
        print('thread running')
        time.sleep(1)

t = threading.Thread(target=run)
t.setDaemon(True)
t.start()

print('main thread')
time.sleep(3)
print('done')

# 线程会在主线程结束时退出
# 如果不设置为守护线程，则线程会一直运行，直到程序结束
