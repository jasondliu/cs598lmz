import threading
threading.stack_size(2**27)
sys.setrecursionlimit(10**7)
thread = threading.Thread(target = main)
thread.start()
