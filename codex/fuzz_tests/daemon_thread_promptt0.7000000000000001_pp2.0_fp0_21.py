import threading
# Test threading daemon
def test_thread():
    print('start')
    time.sleep(10)
    print('end')

if __name__ == '__main__':
    t = threading.Thread(target=test_thread)
    t.setDaemon(True)
    t.start()
    t.join(timeout=5)
    print('main thread')

# Output:
# start
# main thread
# [Finished in 5.0s]
