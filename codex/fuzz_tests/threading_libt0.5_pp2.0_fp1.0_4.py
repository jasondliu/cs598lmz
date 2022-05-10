import threading
threading.stack_size(2**27)
import sys
import os
import math
import random
import time

def run_test(test_name, test_function):
    print test_name,
    sys.stdout.flush()
    t0 = time.time()
    test_function()
    t1 = time.time()
    print " %.3f" % (t1 - t0)

def run_tests(test_functions):
    for test_name, test_function in test_functions:
        run_test(test_name, test_function)

def test_fib(n):
    if n < 2:
        return 1
    else:
        return test_fib(n - 1) + test_fib(n - 2)

def test_fib_loop(n):
    a, b = 1, 1
    for i in range(n):
        a, b = b, a + b
    return a

def test_fib_iter():
    a, b = 1, 1
    while 1:

