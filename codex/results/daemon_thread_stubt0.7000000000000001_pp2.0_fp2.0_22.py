import sys, threading

def run():
    for i in range(99):
        time.sleep(0.1)

if __name__ == '__main__':
    global threadPool
    threadPool = []
    startTime = time.time()
    for i in range(100):
        threadPool.append(threading.Thread(target=run))
    for i in threadPool:
        i.start()
    for i in threadPool:
        i.join()
    print('耗时：', time.time()-startTime)
