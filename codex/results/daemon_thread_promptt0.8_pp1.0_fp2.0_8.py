import threading
# Test threading daemon mode
# After main thread ends, the non-daemon thread still runs.
def func():
    print('function sleep')
    time.sleep(10)
    print('function end')

func_thread = threading.Thread(target=func)
print('before')
func_thread.setDaemon(True)
func_thread.start()
print('ending')
