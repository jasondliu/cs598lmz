import threading
threading.stack_size(67108864)
x = threading.activeCount()
print(x)

 
sys.setrecursionlimit(2 ** 20)
threading._start_new_thread(main,())

# This code will cause infinite loop(due to unending recursion)
"""while True:
    time.sleep(.5)
    pass"""
