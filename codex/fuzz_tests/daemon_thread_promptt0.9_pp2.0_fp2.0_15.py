import threading
# Test threading daemonization
# The process with main thread would exit even if daemon thread has not yet finished
# while the process with no main thread would not
def test(t_id):
    print(t_id)
    print(time.time())
    print('Start')
    time.sleep(10)
    return t_id

# Setting the main thread as a daemon
thread = threading.Thread(name='Test', target=test, args=(1,), daemon=True)
# thread = threading.Thread(name='Test', target=test, args=(1,))
print(thread.start())    # Start the thread

print('Main')
thread.join()  # Wait for the thread to exit
print('Main Exit')

# Check the documentation:
# https://docs.python.org/3.7/library/threading.html#threading.Thread.run
