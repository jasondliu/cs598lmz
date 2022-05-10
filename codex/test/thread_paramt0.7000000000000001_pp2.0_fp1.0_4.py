import sys, threading
threading.Thread(target=lambda: sys.stdout.write('Hello from\nThread 1\n')).start()
threading.Thread(target=lambda: sys.stdout.write('Hello from\nThread 2\n')).start()
threading.Thread(target=lambda: sys.stdout.write('Hello from\nThread 3\n')).start()

# 8.11
def my_range(first=0, last=10, step=1):
    number = first
    while number < last:
        yield number
        number += step

ranger = my_range(1, 5)
for x in ranger:
    print(x)

# 8.12
def my_zip(*seqs):
    seqs = [list(S) for S in seqs]
    res = []
    while all(seqs):
        res.append(tuple(S.pop(0) for S in seqs))
    return res

S1, S2 = "abc", "xyz123"
print(my_zip(S1, S2))


# 8.13
