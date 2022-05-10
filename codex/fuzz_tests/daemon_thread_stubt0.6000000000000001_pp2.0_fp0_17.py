import sys, threading

def run():
    print('Thread started')
    for i in range(10):
        print(i)
        time.sleep(1)
    print('Thread ended')

t = threading.Thread(target=run)
t.start()
print('Main thread ended')
</code>

