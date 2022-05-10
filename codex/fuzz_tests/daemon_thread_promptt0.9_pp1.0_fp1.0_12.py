import threading
# Test threading daemon
daemon_thread = threading.Thread(
        name='daemon_thread', 
        target=factorial_n(5), 
        daemon=True)

# 使用 is_alive() 确认主线程是否运行
print("Before starting the thread")
print("is the thread alive?", daemon_thread.is_alive())

# 启动主线程
daemon_thread.start()
print("After starting the thread")
print("is the thread alive", daemon_thread.is_alive())

# 判断主线程的信息
daemon_thread.join()
# 判断线程运行结果
print("Is the daemon thread alive?", daemon_thread.is_alive())

print("退出主线程")
