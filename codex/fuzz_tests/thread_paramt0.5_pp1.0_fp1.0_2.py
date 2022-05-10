import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\a')).start()

# 使用线程池
from concurrent.futures import ThreadPoolExecutor

def action(max):
    mysum = 0
    for i in range(max):
        print(threading.current_thread().name + '  ' + str(i))
        mysum += i
    return mysum

with ThreadPoolExecutor(max_workers=2) as pool:
    results = list(pool.map(action, range(10, 16)))
    print(results)

# 使用线程池
# from concurrent.futures import ThreadPoolExecutor
#
# def action(max):
#     mysum = 0
#     for i in range(max):
#         print(threading.current_thread().name + '  ' + str(i))
#         mysum += i
#     return mysum
#
# pool = ThreadPoolExecutor(max_workers=2)
# future1 = pool.submit(action, (
