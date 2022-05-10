import threading
# Test threading daemon
# https://www.cnblogs.com/zhaof/p/6171030.html

# 线程的守护进程
# 使用daemon属性
# 只有主线程结束，子线程才会结束
# 如果子线程是守护进程，则子线程会在主线程结束后结束
# 所以主线程不管有没有执行完，都会结束
# 如果主线程结束，子线程还没有执行完，子线程也
