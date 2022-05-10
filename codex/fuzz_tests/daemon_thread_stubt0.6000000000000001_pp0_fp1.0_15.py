import sys, threading

def run():
    while True:
        print("hello")
        time.sleep(1)

for i in range(5):
    t = threading.Thread(target=run)
    t.setDaemon(True)
    t.start()

# 暂停一秒让线程执行
time.sleep(1)
print('main thread end')
