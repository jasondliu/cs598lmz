import threading
# Test threading daemon
def test_thread(name):
    print(name)
    time.sleep(1)
    print(name)

def main():
    # Create thread
    t = threading.Thread(target=test_thread, args=('test',))
    # Set thread daemon
    t.setDaemon(True)
    # Start thread
    t.start()
    # Main thread wait for 2 seconds
    time.sleep(2)
    print('main thread end')

if __name__ == '__main__':
    main()

# Test result:
# test
# main thread end

# Process:
# 1. Create thread
# 2. Set thread daemon
# 3. Start thread
# 4. Main thread wait for 2 seconds
# 5. Main thread end
# 6. Thread end
