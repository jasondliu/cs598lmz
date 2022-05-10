import sys, threading

def run():
    x = list(range(1000000))
    l = threading.Lock()
    thread_count = 4
    def f(n):
        for i, elem in enumerate(x):
            l.acquire()
            x[i] += 1
            l.release()
    threads = []
    for i in range(thread_count):
        t = threading.Thread(target=f, args=[i])
        t.start()
        threads.append(t)
    for t in threads:
        t.join()
    print(x[:10])
    
if __name__ == "__main__":
    run()

# [2000001, 2000002, 2000003, 2000004, 2000005, 2000006, 2000007, 2000008, 2000009, 2000010]
