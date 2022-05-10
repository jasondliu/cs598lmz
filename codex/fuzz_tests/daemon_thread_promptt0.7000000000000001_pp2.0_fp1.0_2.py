import threading
# Test threading daemon by running a thread to kill the main process.


def worker():
    print('Starting worker')
    time.sleep(0.2)
    print('Finished worker')


thread = threading.Thread(target=worker, args=())
thread.setDaemon(True)  # Daemon means the thread will die when the main process terminates
thread.start()
time.sleep(0.1)
print('Checkpoint')
time.sleep(0.2)
print('Bye')

# 运行结果：
# Checkpoint
# Starting worker
# Bye
