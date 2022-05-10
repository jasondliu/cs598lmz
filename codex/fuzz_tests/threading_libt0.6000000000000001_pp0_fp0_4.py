import threading
threading.main_thread().name

#%%
# start a thread and wait for it to finish
def countdown(n):
    while n > 0:
        print('T-minus', n)
        n -= 1
        time.sleep(5)
        
from threading import Thread

t = Thread(target=countdown, args=(10,))
t.start()

#%%
# using a thread as a daemon
def countdown(n):
    while n > 0:
        print('T-minus', n)
        n -= 1
        time.sleep(5)

t = Thread(target=countdown, args=(10,), daemon=True)
t.start()

#%%
# using a thread as a daemon
def countdown(n):
    while n > 0:
        print('T-minus', n)
        n -= 1
        time.sleep(5)

t = Thread(target=countdown, args=(10,), daemon=True)
t.start()
t.join()

#%%
# using a thread as a daemon
def countdown(n):
