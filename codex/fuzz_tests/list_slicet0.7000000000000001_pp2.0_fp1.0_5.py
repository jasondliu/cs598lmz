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
#print keepali0e

from __future__ import with_statement
from functools import wraps
def error_logging(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        try:result=func(*args,**kwargs)
        except Exception,e:
            err_msg=e.message
            err_traceback=sys.exc_info()
            print err_msg,err_traceback
            sys.exit(1)
        return result
    return wrapper

def func():
    return 1
@error_logging
def func1():
    print a
func1()

def func():
    return 1
@error_logging
def func1():
    print a
try:
    func1()
except Exception,e:
    print e

import time
time.sleep(0.5)
import time
time.sleep(1)
import time
time.sleep(1)
import time
time.sleep(1)
import time
time.sleep(1)
import time
time.sleep(1)
