import select
# Test select.select
s, _, _ = select.select([], [], [], 0.1)
print(s)

import psutil
# Test psutil
p = psutil.Process()
print(p.status())

from multiprocessing import Process
from multiprocessing.sharedctypes import Value, Array
# Test multiprocessing
def f(n, a):
    n.value = 3.1415927
    for i in range(len(a)):
        a[i] = -a[i]

num = Value('d', 0.0)
arr = Array('i', range(10))
p = Process(target=f, args=(num, arr))
p.start()
p.join()
print(num.value)
print(arr[:])

import win32com.client
# Test win32com
xl = win32com.client.Dispatch("Excel.Application")
xl.Visible = True
xl.Workbooks.Open('C:\\test\\test.xlsx')

"""

"""
