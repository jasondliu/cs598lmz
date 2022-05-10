import select
# Test select.select
# print("Reading")
# r, w, x = select.select([sys.stdin], [], [], 2)
# print("r:", r)
# print("Writing")
# r, w, x = select.select([], [sys.stdout], [], 2)
# print("w:", w)
# print("All I/O")
# r, w, x = select.select([sys.stdin, sys.stdout], [], [], 2)
# print("r + w:", r, w)
# 
# # Test select.poll
# p = select.poll()
# p.register(sys.stdin)
# p.register(sys.stdout, select.POLLOUT)
# print("poll():", p.poll(2))
# 
# # Test select.epoll

#import socket

# while True:
#     # Get a listing of all the files, then do an arbitrary
#     # action to each of them.
#     for f in os.listdir("."):
#         process_file(f)
