import threading
# Test threading daemon

def thread_func():
    global count
    for i in range(10):
        count += 1
        print(count)
        time.sleep(1)

count = 0

thread = threading.Thread(target=thread_func)
thread.setDaemon(True)
thread.start()

print('Main thread')

# Main thread is not waiting for thread_func to finish
# It will end
