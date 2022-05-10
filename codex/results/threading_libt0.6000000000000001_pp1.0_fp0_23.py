import threading
threading.Thread(target=fun).start()

# 加锁
lock = threading.Lock()

lock.acquire()
lock.release()

# 全局解释器锁，python的多线程只能用于IO操作，不能用于计算密集型任务
# 线程同步，互斥锁
# python中的Queue模块中的Queue类实现了一个线程安全的队列，队列中的任何元素都在队列的两端操作，先进先出

# Queue模块中的LifoQueue类实现了一个
