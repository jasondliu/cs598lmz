import select
# Test select.select()
inlist, outlist, errlist = select.select([sys.stdin], [], [], 30)

# Indicate which file descriptors are ready
# for reading
# if inlist:
#     for fd in inlist:
#         print(fd.read())
# else:
#     print("No input!")

# Test select.poll()
p = select.poll()
p.register(sys.stdin, select.POLLIN)
event_list = p.poll(30)  # Wait for 30 ms

# Indicate which file descriptors are ready
# for reading
# for fd, event in event_list:
#     if fd == sys.stdin.fileno():
#         # Handle keyboard input
#         print(fd.read())
#     else:
#         # Handle other events
#         pass

# Test select.epoll()
# p = select.epoll()
# p.register(sys.stdin, select.EPOLLIN)
# event_list = p.poll(30)  # Wait for 30 ms
