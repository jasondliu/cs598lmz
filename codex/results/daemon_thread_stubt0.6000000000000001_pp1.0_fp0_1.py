import sys, threading

def run():
    global x
    x = 0
    for i in range(10000000):
        x += 1

if __name__ == '__main__':
    t1 = threading.Thread(target=run)
    t2 = threading.Thread(target=run)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(x)

# 这也是线程不安全的例子，因为两个线程同时对同一个变量进行操作，
# 但是不同的是这两个线程并没有共享同一个对象，而是同时修改了同一个变量，这也是线程不安全的一
