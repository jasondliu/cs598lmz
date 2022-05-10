import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
while lst:keepali0e.append(lst[:])

import thread
_interrupt=False

def handle_interrupt():
    global _interrupt
    _interrupt=True

def raise_interrupt():
    handle_interrupt()
    raise ValueError

def subinterp_main(replace):
    handle_interrupt()

def run_in_interpreter2(replace):
    subinterp_main(replace)
    while not _interrupt:
        pass

def run_in_interpreter(replace):
    thread.start_new_thread(run_in_interpreter2,(replace,))
