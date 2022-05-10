import sys, threading

def run():
    while True:
        print(threading.current_thread().name)

if __name__ == '__main__':
    for i in range(100):
        t = threading.Thread(target=run)
        t.start()
</code>
The output is:
<code>Thread-1
Thread-2
Thread-3
Thread-4
Thread-5
Thread-6
Thread-7
Thread-8
Thread-9
Thread-10
Thread-11
Thread-12
Thread-13
Thread-14
Thread-15
Thread-16
Thread-17
Thread-18
Thread-19
Thread-20
Thread-21
Thread-22
Thread-23
Thread-24
Thread-25
Thread-26
Thread-27
Thread-28
Thread-29
Thread-30
Thread-31
Thread-32
Thread-33
Thread-34
Thread-35
Thread-36
Thread-37
Thread-38
Thread-39
Thread-40
Thread-41
Thread-42
Thread-43
Thread-44
Thread-45
Thread-46
Thread
