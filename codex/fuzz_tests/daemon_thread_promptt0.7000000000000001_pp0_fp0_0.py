import threading
# Test threading daemon
# 引入threading模块中的Thread类，用于生成线程实例
# 生成thread实例的第二个参数daemon指定守护进程
# 值为True，当主线程结束时，该线程也会结束
# 值为False，当主线程结束时，该线程不会结束
# def daemo():
#     print("daemon thread starting")
#     time.sleep(2)
#     print("daemon thread ending")
#
# d = threading.Thread(target=daemo,daemon=True)
# d.start()
# print("main thread ending")
# 可以
