import io
class File(io.RawIOBase):
    def __init__(self, f):
        self.f = f
    def read(self, n=-1):
        return self.f.read(n).encode()
    def write(self, b):
        return self.f.write(b.decode())
sys.stdin = File(sys.stdin)
sys.stdout = File(sys.stdout)
sys.stderr = File(sys.stderr)

# read
n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# solve
# a, b = sorted(a), sorted(b)
# for i in range(m):
#     for j in range(n):
#         if b[i] >= a[j] and b[i] - a[j] < b[i] - a[j + 1]:
#             a[j] = b[i]
#             break
#         if j == n - 1:
#             a.append
