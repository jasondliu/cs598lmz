import threading
threading.stack_size(67108864)

# 创建一个线程
t = threading.Thread(target=run_thread, args=(5,))

# 启动线程
t.start()

# 等待线程结束
t.join()

print("线程执行完毕")
