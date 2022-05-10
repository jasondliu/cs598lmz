import sys, threading
threading.Thread(target=lambda: sys.stdout.write("Hello\n")).start()

# 计算密集型任务用多线程有助于提升性能。
# 例如，计算圆周率可以采用数学公式：
# pi/4 = 4*arctan(1/5) - arctan(1/239)
# 也可以采用下面的算法计算：
# https://zh.wikipedia.org/wiki/%E5%9F%83%E6%8B%89%E6%89%98%E6%96%AF%E7%89%B9%E5%B0%BC%E6%96%B9%E6%B3%95
import time
