import threading
# Test threading daemon
#test = threading.Thread(target=work, args=(10,))
#test.setDaemon(True)
#test.start()

# Test normal threading
#work(20)

# Test threading pool
#pool = ThreadPool(10)
#pool.map(work, range(20))

# Test multiprocessing pool
#pool = multiprocessing.Pool(10)
#pool.map(work, range(20))

# Test multiprocessing thread pool
#pool = multiprocessing.pool.ThreadPool(10)
#pool.map(work, range(20))

# Test multiprocessing process pool
pool = multiprocessing.pool.Pool(10)
pool.map(work, range(20))
