from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.size

# 可以用一个类来模拟其他类的实例，而不必通过继承
class BinaryNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def binary_search(node, target):
    if node is None:
        return False
    if node.value == target:
        return True
    elif node.value > target:
        return binary_search(node.left, target)
    else:
        return binary_search(node.right, target)

# 使用Mock类来模拟一个BinaryNode实例
from unittest.mock import Mock
root = Mock(spec=BinaryNode)
root.value = 10
