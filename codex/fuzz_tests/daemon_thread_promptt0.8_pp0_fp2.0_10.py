import threading
# Test threading daemon
# 需要注意的是，在子线程中运行的代码，不管有没有运行完成，当主线程结束时，子线程也会被强制终止。
# 这个例子中，主线程启动了一个子线程，子线程会在5秒后结束。但是当主线程在3秒的时候结束了，子线程也会在3秒的时候结束。

def run(n):
    print('task',n)
    time.sleep(2)
