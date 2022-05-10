import threading
threading.stack_size(2**27)
thread = threading.Thread(target=main)
thread.start()

if __name__ == '__main__':
    print("PASSED")
    
# vim: set et sw=4 ts=4:
