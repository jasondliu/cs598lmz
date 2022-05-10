import mmap

f = open("data/rosalind_bins.txt", 'r')

map = mmap.mmap(f.fileno(), 0, prot=mmap.PROT_READ)

n,m = map.readline()[:-1].split()
n = int(n)
m = int(m)

A_str = map.readline()[:-1]
A = map.readline()[:-1].split()
A = [int(x) for x in A]

B_str = map.readline()[:-1]
B = map.readline()[:-1].split()
B = [int(x) for x in B]

map.close()
f.close()

def binarySearch(lst, key):
    if len(lst) == 0:
        return -1
    start = 0
    end = len(lst) - 1
    while start <= end:
        mid = (start + end) // 2
        if key < lst[mid]:
            end = mid - 1
        elif
