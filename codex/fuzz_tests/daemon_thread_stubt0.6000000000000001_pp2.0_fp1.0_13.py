import sys, threading

def run():
    while True:
        time.sleep(1)
        print(threading.get_ident())

thr = threading.Thread(target=run)
thr.start()

print(threading.get_ident())
print(thr.ident)

# 这是启动了线程后，新线程与主线程的线程 ID
# 这是主线程的线程 ID
# 这是新线程的线程 ID
# 新线程的线程 ID 与主线程的线程 ID 是不同的
