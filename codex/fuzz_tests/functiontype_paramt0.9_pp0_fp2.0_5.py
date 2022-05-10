from types import FunctionType
list(FunctionType(hex.__code__,globals(),'hex').__globals__.keys())[:5]

#Q51： 调用Square实例的__repr__方法，然后解析返回的字符串以重建该实例
class Square:
    def __init__(self,side):
        self.side = side
    def __repr__(self):
        return 'Square(side={!r})'.format(self.side)
    def __eq__(self,other):
        return self.side == other.side
Square(5)

_,side = eval(Square(5).__repr__())
sq = Square(side)

#Q52： 使用assertIsInstance来检查代码片段中对象的类型
int(True)],int(False)),
int(sq))

#Q
