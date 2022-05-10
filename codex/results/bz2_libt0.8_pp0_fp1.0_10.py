import bz2
bz2.decompress(b)

#compile function

def fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def fib_seq(n):
    seq = []
    for i in range(n+1):
        seq.append(fib(i))
    return seq
fib_seq(10)

import random
def choose_random_items(n, stream):
    random_items = []
    for i in range(n):
        random_index = int(random.random() * len(stream))
        random_items.append(stream[random_index])
    return random_items

choose_random_items(10, [1,2,3,4,5,6,7,8,9,10])

stream = [1,2,3,4,5,6,7,8,9,10]
a = map(hex, stream)
print(a)
b = map
