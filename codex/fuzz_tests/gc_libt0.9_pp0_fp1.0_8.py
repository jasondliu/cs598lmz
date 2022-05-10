import gc, weakref
from collections import defaultdict


class LeakTestCase(unittest.TestCase):
    """
        destory(), restore() 上篇博客有讲，就是需要注意的地方。
        如果有循环引用，就无法被回收，那么就要注意，是否在单元测试中使用了restore()方法？
        restore()方法，又将该对象恢复到了strong reference中，那么在tearDown()方法中就需要使用destory()方法，
        如果不用，则会一直添加到gc.garbage 中。
    """
