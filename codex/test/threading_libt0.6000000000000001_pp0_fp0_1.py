import threading
threading.currentThread()

# from threading import currentThread
# currentThread()

# 守护线程
def action(max):
    for i in range(max):
        print(threading.current_thread().name + " " + str(i))

t = threading.Thread(target=action, args=(100,), name="新线程")
t.setDaemon(True)
t.start()

for i in range(10):
    print(threading.current_thread().name + " " + str(i))

if threading.current_thread() == t:
    print("这是新线程")
else:
    print("这是主线程")

# 线程同步
# 全局变量
g_num = 0
def test1():
    global g_num
    for i in range(1000000):
        g_num += 1

