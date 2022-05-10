import sys, threading

def run():
    global end, end_mutex
    for i in range(10000000):
        end += 1
        end_mutex.acquire()
        end_mutex.release()

if __name__ == '__main__':
    end = 0
    end_mutex = threading.Lock()
    t1 = threading.Thread(target=run)
    t2 = threading.Thread(target=run)
    t1.start()
    t2.start()
    print end
