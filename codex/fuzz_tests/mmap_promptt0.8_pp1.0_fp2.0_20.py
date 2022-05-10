import mmap
# Test mmap.mmap
with open("in.txt") as f:
    inp = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
    txt = eval("["+inp.readline().decode("utf-8").strip()+"]")
print(txt)

N, K = txt[0], txt[1]
print("N = " + str(N))
print("K = " + str(K))

# Solution

result = 0
# for i in range(K-1, N):
#     result += N - i
#     # print("i = " + str(i))
#     # print("result = " + str(result))
for i in range(1, K):
    result += i*(N-i)
result += (N-K+1)*K

print(result % (10**9+7))

# Submission
o = open("out.1.txt", "w")
o.write(str(result % (10**9+7)))
