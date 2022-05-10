import threading
threading.activeCount()

def plus():
    global n
    for i in range(1000000):
        n += 1

def minus():
    global n
    for i in range(1000000):
        n -= 1

t1 = threading.Thread(target=plus)
t1.start()
t2 = threading.Thread(target=minus)
t2.start()
t1.join()
t2.join()
print(n)

#특정 시간마다 주기적으로 실행하기
import threading, time

def loop1(in1):
    print("Start loop1", in1)
    print("End loop1")

def loop2(in1, in2):
    print("Start loop2", in1, in2)
    print("End loop2")

def main():
    print("Start main threading")
    t1 = threading.Thread(target=loop1, args=("A
