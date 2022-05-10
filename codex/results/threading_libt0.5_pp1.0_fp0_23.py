import threading
threading.Thread(target=lambda:input()).start()

# from threading import Thread
# Thread(target=lambda:input()).start()

# from multiprocessing import Process
# Process(target=lambda:input()).start()

# from multiprocessing.dummy import Pool
# Pool(1).map(lambda:input(),[None])

# from multiprocessing.dummy import Pool as ThreadPool
# ThreadPool(1).map(lambda:input(),[None])

# import concurrent.futures
# with concurrent.futures.ThreadPoolExecutor(max_workers=1) as executor:
#     future = executor.submit(lambda:input())
#     future.result()

# import concurrent.futures
# with concurrent.futures.ProcessPoolExecutor(max_workers=1) as executor:
#     future = executor.submit(lambda:input())
#     future.result()

# from gevent.pool import Pool
# Pool(1).map(lambda:input(),[None])

# from gevent
