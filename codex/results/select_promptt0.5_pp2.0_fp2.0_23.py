import select
# Test select.select()

def slow_systemcall():
    select.select([], [], [], 0.1)

start = time.time()
for _ in range(5):
    slow_systemcall()
end = time.time()
print('Took %.3f seconds' % (end - start))

# 使用多进程
from multiprocessing import Pool

start = time.time()
pool = Pool(processes=5)
for _ in range(5):
    pool.apply_async(slow_systemcall)
pool.close()
pool.join()
end = time.time()
print('Took %.3f seconds' % (end - start))


# 使用多线程
from threading import Thread

start = time.time()
threads = []
for _ in range(5):
    thread = Thread(target=slow_systemcall)
    thread.start()
    threads.append(thread)
for thread in threads:
    thread.join()
end = time.time()
