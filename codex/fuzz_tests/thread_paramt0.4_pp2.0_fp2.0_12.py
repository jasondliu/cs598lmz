import sys, threading
threading.Thread(target=lambda: sys.stdout.write("hello\n")).start()

#
# 使用协程
#
# 协程的最大特点就是一个线程执行。
#
# 协程看上去也是子程序，但执行过程中，在子程序内部可中断，然后转而执行别的子程序，在适当的时候再返回来接着执行。
#
# 注意，在一个子程序中中断，去执行其他子程序，不是函数调用，有点类似
