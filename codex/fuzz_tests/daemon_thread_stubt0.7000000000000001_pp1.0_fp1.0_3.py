import sys, threading

def run():
    while True:
        print('Threading')
        time.sleep(1)

# 创建一个子线程
t = threading.Thread(target=run)
# 判断子线程是否存活
print(t.is_alive())
# 子线程启动
t.start()
print(t.is_alive())
t.join()
print(t.is_alive())

t2 = threading.Thread(target=run)
t2.daemon = True
t2.start()
print(t2.is_alive())
