import mmap

n = 100000

max_value = 3

a = np.random.randint(-max_value, max_value, n)

start = time()

np.array(np.trunc(a*1.0/max_value), dtype=np.int8)

print time() - start

start = time()

with open("F:\\test.bin", "rb+") as f:
    mem = mmap.mmap(f.fileno(),
