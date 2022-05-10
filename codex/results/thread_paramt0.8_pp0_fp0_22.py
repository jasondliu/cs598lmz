import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\x1b[1;32mHello World\x1b[0m\n')).start()

wall = [int(i) for i in input().split()]

N = wall[0]
D = wall[1]

# print(N)
# print(D)

B = [int(i) for i in input().split()]

# print(B)

B_sum = sum(B)

# print(B_sum)

max = 0
temp = 0

for i in range(N-D+1):
    temp = B_sum
    start = i
    end = i+D
    # print(B[start:end])
    temp = temp - sum(B[start:end])
    if(temp > max):
        max = temp

print(max)
