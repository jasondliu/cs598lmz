import threading
# Test threading daemonization
threading.Thread(target=thread_func).start()
time.sleep(1)

# Test forking
if os.fork() == 0:
    time.sleep(1)
    config.GET_LOGGER().error("Child forked")
