import threading
# Test threading daemon
def test_thread():
    print("Threading test")

t = threading.Thread(target=test_thread)
t.daemon = True
t.start()

# Test multiprocessing daemon
def test_process():
    print("Multiprocessing test")

p = multiprocessing.Process(target=test_process)
p.daemon = True
p.start()

# Test multiprocessing pool daemon
def test_pool():
    print("Multiprocessing pool test")

pool = multiprocessing.Pool(1, test_pool)
pool.daemon = True
pool.start()

# Test multiprocessing pool map daemon
def test_pool_map():
    print("Multiprocessing pool map test")

pool_map = multiprocessing.Pool(1, test_pool_map)
pool_map.daemon = True
pool_map.map(test_pool_map, range(1))

# Test multiprocessing pool apply daemon
def test_pool_apply():
    print("Mult
