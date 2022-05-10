import sys, threading

def run():
    while True:
        print("Thread 1")

thread1 = threading.Thread(target=run)
thread1.start()

while True:
    print("Thread 2")
</code>
Output:
<code>Thread 1
Thread 2
Thread 1
Thread 2
Thread 1
Thread 2
Thread 1
Thread 2
Thread 1
Thread 2
Thread 1
Thread 2
Thread 1
Thread 2
Thread 1
Thread 2
Thread 1
Thread 2
Thread 1
Thread 2
Thread 1
Thread 2
Thread 1
Thread 2
Thread 1
Thread 2
Thread 1
Thread 2
Thread 1
Thread 2
Thread 1
Thread 2
Thread 1
Thread 2
Thread 1
Thread 2
Thread 1
Thread 2
Thread 1
Thread 2
Thread 1
Thread 2
Thread 1
Thread 2
Thread 1
Thread 2
Thread 1
Thread 2
Thread 1
Thread 2
Thread 1
Thread 2
Thread 1
Thread 2
Thread 1
Thread 2
Thread 1
Thread 2
Thread 1
Thread 2
Thread 1
Thread 2
Thread 1
Thread 2
Thread 1
Thread 2
Thread 1

