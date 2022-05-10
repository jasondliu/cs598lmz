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
'''

import os
import sys
import time
import gc
import weakref
import threading
import multiprocessing
import traceback
import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

import _testcapi

def run_test(test_code, timeout=100):
    '''
    Run the test code in a subprocess, with a timeout.
    '''
    # We need to run the test in a subprocess, because we want to
    # be sure that we are not holding any Python reference to the
    # objects we are testing.
    def f():
        # The test code will run in this process.
        gc.disable()
        try:
            exec(test_code, globals())
        except:
            logger.error(traceback.format_exc())
        finally:
            gc.enable()

    # Start the test process.
    p = multiprocessing.Process(target=f)
    p.start()

    # Wait for the test
