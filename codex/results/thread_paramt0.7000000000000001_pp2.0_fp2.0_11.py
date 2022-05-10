import sys, threading
threading.Thread(target=lambda: sys.stdout.write("foo\n")).start()

# 为了在Python中使用多线程，只需要构造一个Thread实例并将函数传给它。为此，我们需要引入threading模块。
# 在这个例子中，我们创建了一个Thread的实例t。接下来，我们调用t.start()以启动新线程。
# 请注意，t.join()的调用是一个阻塞调用，它会等待新线程结束后再执行后
