import threading
threading.Thread(target=lambda: print(1)).start()

# 创建多个线程
def f(i):
    print(i)

threads = []
for i in range(10):
    t = threading.Thread(target=f, args=(i,))
    threads.append(t)
    t.start()

# 线程同步
# 线程同步的最简单的方式是使用 threading.Lock 对象。
# 在需要保护的代码块前调用 acquire() 方法，在代码块执行完毕后调用 release() 方法。
# 如果一个线程调用了 acquire() 方法，其他
