import sys, threading
threading.Thread(target=lambda: os.kill(os.getpid(), 9)).start()
time.sleep(10)
class A(object):
    """
    the expected output of the test below is:
    works
    works
    Traceback (most recent call last):
     File "killable_thread.py", line 8, in <module>
       class A(object):
     File "killable_thread.py", line 10, in A
       time.sleep(0.1)
     File "/usr/lib/python2.5/threading.py", line 323, in join
       self.__block.wait(timeout)
     File "/usr/lib/python2.5/threading.py", line 264, in wait
       _sleep(delay)
    """
    time.sleep(0.1)
