import sys, threading
threading.Thread(target=lambda: sys.stdout.write("1\n")).start()
threading.Thread(target=lambda: sys.stderr.write("2\n")).start()

#  执行结果
#  2
#  1

#  上面代码在同一个线程中，两个线程是交替执行的，而不是同时执行的，这说明线程之间的共享变量被隔离了，线程自己的变量是隔离的。
#  多个线程之间共享变量的方式，有全局变量、实例变量、类变量
