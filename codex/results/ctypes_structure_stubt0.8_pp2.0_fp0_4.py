import ctypes

class S(ctypes.Structure):
    x = ctypes.c_ubyte
    if sys.version_info[0] < 3:
        y = ctypes.c_ushort
    else:
        y = ctypes.c_ulong

THREADS = 20

def worker(a, i, n):
    for j in range(n):
        a[i].x = j
        a[i].y = 2*j

a = (S*THREADS)()

t0 = time.time()
t = [ threading.Thread(target=worker, args=(a,i,40)) for i in range(THREADS) ]
[ t.start() for t in t]
[ t.join() for t in t]
print("Python threads on %s: %.3f" % (sys.version, time.time() - t0))

print("done")
