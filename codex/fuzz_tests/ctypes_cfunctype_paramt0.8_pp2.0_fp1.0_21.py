import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None, ctypes.c_int, ctypes.c_void_p)
FUN = FUNTYPE(lambda i, s: print(i, s))
shm = shm.SharedMemory.create(FUN, 4, 32*32, False)
N = 10000

t = time.process_time()
for i in range(N):
    shm.begin()
    shm.data[0] = i
    shm.end()
print(time.process_time() - t)

t = time.process_time()
for i in range(N):
    shm.put(i)
print(time.process_time() - t)

t = time.process_time()
for i in range(N):
    shm.begin()
    shm.data[0] = i
    shm.end()
print(time.process_time() - t)

t = time.process_time()
for i in range(N):
    shm.put(i)
print(time.process_time() - t)

t = time
