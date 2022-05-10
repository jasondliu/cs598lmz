import sys, threading
threading.Thread(target=lambda:sys.stdout.write('\n'.join(map(str, [i for i in range(2000001)])))).start()

"""
num_list = [i for i in range(2000001)]
print(num_list)
"""

#start_time = timeit.default_timer()

#elapsed = timeit.default_timer() - start_time
#print(elapsed)

"""
def sum_of_n(n):
    start_time = timeit.default_timer()
    the_sum = 0
    for i in range(1, n+1):
        the_sum = the_sum + i
    elapsed = timeit.default_timer() - start_time
    return the_sum, elapsed

for i in range(1, 10001):
    print(i, ' ', sum_of_n(i))
"""

