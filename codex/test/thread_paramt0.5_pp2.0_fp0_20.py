import sys, threading
threading.Thread(target=lambda: sys.stdout.write(input())).start()

# another way
# import threading
# input_thread = threading.Thread(target=input, args=())
# input_thread.start()
# input_thread.join()

# another way
# from threading import Thread
# Thread(target=input).start()

# another way
# from multiprocessing.pool import ThreadPool
# pool = ThreadPool(processes=1)
# async_result = pool.apply_async(input) # runs in *only* one process
# async_result.get() # get the return value from your function.

# another way
# import multiprocessing
# p = multiprocessing.Process(target=input)
# p.start()
# p.join()

# another way
# import multiprocessing
# p = multiprocessing.Pool(1)
# p.apply(input)

# another way
# import subprocess
# subprocess.call([sys.executable, '-c', 'input()'])

# another way
