import threading
threading.current_thread()

#因此，多线程程序的执行流程就是一个洋葱圈。

# Python的标准库提供了两个模块：_thread和threading，_thread是低级模块，
# threading是高级模块，对_thread进行了封装。绝大多数情况下，我们只需要使用threading这个高级模块。

# 启动一个线程就是把一个函数传入并创建Thread实例，然后调用start()
