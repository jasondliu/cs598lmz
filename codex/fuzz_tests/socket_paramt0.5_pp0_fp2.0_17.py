import socket
socket.if_indextoname(3)

socket.if_nametoindex('en0')

import threading

def worker():
    """thread worker function"""
    print 'Worker'
    return

threads = []
for i in range(5):
    t = threading.Thread(target=worker)
    threads.append(t)
    t.start()

# import itertools
#
# for i in itertools.count(0):
#     print i
#     if i > 10:
#         break
#
# for i in itertools.repeat('hi', 10):
#     print i
#
# for i in itertools.cycle([1,2,3]):
#     print i
#     if i > 10:
#         break
#
# for i in itertools.permutations([1,2,3]):
#     print i
#
# for i in itertools.combinations([1,2,3,4],2):
#     print i
#
# for i in itertools.product([1,2,3,
