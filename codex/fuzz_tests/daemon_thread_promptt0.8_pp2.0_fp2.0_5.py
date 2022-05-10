import threading
# Test threading daemonic
def run_without_daemonic():
    print('Test threading daemonic:')
    print('> create a thread and run in background')
    print('')
    def foo():
        print('foo start')
        time.sleep(2)
        print('foo end')
    bar = threading.Thread(target=foo)
    # print(bar.is_alive())
    bar.start()
    # print(bar.is_alive())
    print('main thread: sleep 3s')
    time.sleep(3)
    # print(bar.is_alive())
    print('main thread: end')
    print('')

# Test threading daemonic
def run_with_daemonic():
    print('Test threading daemonic:')
    print('> create a thread with daemonic and run in background')
    print('')
    def foo():
        print('foo start')
        time.sleep(2)
        print('foo end')
    bar = threading.Thread(target=foo, daemon=True)
    # print(
