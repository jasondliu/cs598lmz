import sys, threading
threading.Thread(target=lambda: sys.stdout.write("Thread 1\n")).start()
threading.Thread(target=lambda: sys.stdout.write("Thread 2\n")).start()

#  13.2.1.1. The Thread.daemon Attribute

#  13.2.1.2. The Thread.join() Method

#  13.2.1.3. The threading.active_count(), threading.enumerate(), and threading.current_thread() Functions

#  13.2.1.4. The threading.settrace() and threading.setprofile() Functions

#  13.2.1.5. The threading.local Class

x = threading.local()
x.number = 42
def foo():
    print(x.number)
foo()

#  13.2.2.1. The threading.Condition Class

c = threading.Condition()
c.notify_all()
c.release()
with c:
    c.wait()
c.wait_for(lambda: False)
c.wait_for
