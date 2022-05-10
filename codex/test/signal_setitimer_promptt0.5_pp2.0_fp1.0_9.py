import signal
# Test signal.setitimer()
#
# 参考：
# http://docs.python.org/2/library/signal.html#signal.setitimer
#
# 在Python中，不能在函数内部设置定时器，否则会报错
# OSError: [Errno 22] Invalid argument
#
# 到底是什么原因呢？
# 参考：
# http://stackoverflow.com/questions/492519/timeout-on-a-function-call
# http://stackoverflow.com/questions/444966/python-how-do-you-kill-threads

