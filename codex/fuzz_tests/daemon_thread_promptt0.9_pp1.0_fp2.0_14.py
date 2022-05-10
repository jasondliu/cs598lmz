import threading
# Test threading daemonic mode.
# This means that when the program exits all the threads spawned
# will be killed.


def print_data(_str, delay):
    for i in range(4):
        time.sleep(delay)
        print(_str)

if __name__ == '__main__':
    t = threading.Thread(target=print_data, args=("hello", 2))
    t2 = threading.Thread(target=print_data, args=("big ", 1))
    t.daemon = True
    t2.daemon = True
    t.start()
    t2.start()
    time.sleep(10)
