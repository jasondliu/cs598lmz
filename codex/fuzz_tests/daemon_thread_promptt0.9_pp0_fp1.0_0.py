import threading
# Test threading daemon
def func():
    print("Start waiting...")
    time.sleep(2)
    print("End waiting")

for i in range(3):
    t = threading.Thread(target=func)
    #t.setDaemon(True) # 如果这里不加，子线程的结束会影响主线程的结束。与主线程的线程类型一致
    t.start()

print("Main Thread")

# 使用协程
def func2():
    yield("Do something") # 什么都不做
    print("End waiting2")

generator = func2()
next(generator)

# 使用协程进行串行
import asyncio
@asyncio.coroutine
def func3():
    print("Start waiting3")

