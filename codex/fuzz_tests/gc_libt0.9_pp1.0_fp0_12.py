import gc, weakref
#
# c = weakref.WeakKeyDictionary()
# c['key1'] = 1
# c['key2'] = 2
# print(c)
# c['key1'] = 'new value'
# print(c)
# del c['key1']
# print(c)


# print(('%d%%' % 100))

# a = [1,2,3]
# b = a
# del a
# print(b)

# import weakref
# s1 = {1, 2, 3}
# s2 = s1
# def bye():
#     print('Gone with the wind...')
#
# ender = weakref.finalize(s1, bye)
# ender.atexit = False
# print(s1)
# del s1
# ender.atexit = True
# print(s2)
# del s2


import shelve
from time import time
from contextlib import closing
from threading import Thread
from random import randrange

with closing(shelve.open('test_shelf
