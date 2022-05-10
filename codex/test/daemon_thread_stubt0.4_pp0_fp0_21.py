import sys, threading

def run():
    global num
    for i in range(100000):
        num += 1

num = 0
thread1 = threading.Thread(target=run)
thread2 = threading.Thread(target=run)
thread1.start()
thread2.start()
thread1.join()
thread2.join()
print(num)
