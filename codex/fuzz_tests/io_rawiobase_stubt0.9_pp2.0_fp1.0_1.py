import io
class File(io.RawIOBase):
    def write(self):
        pass
n = File()
f = io.TextIOWrapper(n)
f.write("hello\n")

import unittest
class TestCase(unittest.TestCase):
    def test_it(self):
        self.assertEqual(True, False)

import random
for a in range(10):
    # print(a)
    print(random.random())

# 希望对对象的方法进行调用的时候， 要求某些参数一定要传
# 不允许有默认值， 一定要传
# 在方法调用之前， 不允许修改参数
class A:
    def __init__(self):
        self.x = 0
    def set_x(self
