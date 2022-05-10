from types import FunctionType
a = (x for x in [1])
print(type(a))
print(type(isinstance))
print(type(FunctionType))

# 判断是否是某种类型
print(isinstance(a, GeneratorType))
print(isinstance(isinstance, FunctionType))

# 测试模块
import unittest
from functools import reduce

class TestCount(unittest.TestCase):
    def setUp(self):
        print('setUp...')

    def tearDown(self):
        print('tearDown...')

    # 类似构造函数
    @classmethod
    def setUpClass(cls):
        print('setUpClass...')

    # 类似析构函数
    @classmethod
    def tearDownClass(cls):
        print('tearDownClass...')

    def test_reduce(self):
        self.assertEqual(reduce(lambda x, y: x+y
