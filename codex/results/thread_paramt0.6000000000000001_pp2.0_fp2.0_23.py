import sys, threading
threading.Thread(target=lambda:sys.stdout.write(str(int(input())+int(input())))).start()
'''

# 6.3.4 多线程与多进程

# 线程和进程都是计算机操作系统中两个最基本的单位。进程是操作系统管理的，线程是CPU管理的。
# 我们可以把线程看作进程中的一个实体，进程就是线程的集合。

# 我们可以通过threading模块来实现多线程。下面的代
