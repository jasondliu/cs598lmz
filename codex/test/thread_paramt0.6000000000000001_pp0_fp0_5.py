import sys, threading
threading.Thread(target=lambda: sys.stdout.write("threading.Thread\n")).start()
# threading.Timer(0, lambda: sys.stdout.write("threading.Timer\n")).start()
# threading.current_thread()

def do_work():
    sys.stdout.write("do_work\n")

def test_threading():
    t = threading.Thread(target=do_work)
    t.start()
    t.join()

def test_threading_timer():
    t = threading.Timer(0, do_work)
    t.start()
    t.join()

# def test_threading_timer_cancel():
#     t = threading.Timer(5, do_work)
#     t.start()
#     t.cancel()

# 如果不join，会出现主线程结束而子线程未执行的情况
test_threading()
test
