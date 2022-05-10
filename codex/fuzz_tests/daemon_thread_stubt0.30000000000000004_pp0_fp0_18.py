import sys, threading

def run():
    while True:
        print(threading.current_thread().name)

t1 = threading.Thread(target=run, name='Thread1')
t2 = threading.Thread(target=run, name='Thread2')
t3 = threading.Thread(target=run, name='Thread3')

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()
