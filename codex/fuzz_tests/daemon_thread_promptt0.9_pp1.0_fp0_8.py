import threading
# Test threading daemon

class A(threading.Thread):
    def run(self):
        while True:
            print("A")
            time.sleep(1)

class B(threading.Thread):
    def run(self):
        while True:
            print("B")
            time.sleep(1)

a = A()
b = B()
a.daemon = True
b.daemon = True
a.start()
b.start()
time.sleep(3)
print("end")

# 主线程在1秒后结束，子线程因为设置成daemon的
# 也会停止，所以打印出A 三次后就结束了

# 可以看出，如果主线程运行时间久一点，
