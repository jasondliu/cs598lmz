import sys, threading

def run():
    for i in range(5):
        print(threading.current_thread().getName(), i)

t1 = threading.Thread(target=run)
t2 = threading.Thread(target=run)

t1.start()
print('thread', t1.is_alive())
t2.start()

# If you call join in a loop then the errors like that
# ''Traceback (most recent call last):
#   File "thread_join.py", line 16, in <module>
#     if not t1.isAlive() and not t2.isAlive():
# RuntimeError: cannot join thread before it is started''
# This is because, start() starts the thread by setting thread state to 
# running. It then invokes Run() in the new thread
# So, if you call join() before calling start() an error will be raised as
# it tries to join the thread before it is started
# refer threadpython for more info

# if t1.is_alive() and t2.is_alive():
if not t1.is_
