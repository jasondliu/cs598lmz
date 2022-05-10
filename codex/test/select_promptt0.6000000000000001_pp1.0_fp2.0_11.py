import select
# Test select.select
print("Testing select.select()")
print("\tAll events:")
read_list, write_list, error_list = select.select([sys.stdin], [], [], 2)
print("\tRead events:")
read_list, write_list, error_list = select.select([sys.stdin], [], [], 2)
print("\tWrite events:")
read_list, write_list, error_list = select.select([], [sys.stdout], [], 2)
print("\tError events:")
read_list, write_list, error_list = select.select([], [], [sys.stdout], 2)

# Test select.poll
print("Testing select.poll()")
poll = select.poll()
poll.register(sys.stdin.fileno(), select.POLLIN)
poll.register(sys.stdout.fileno(), select.POLLOUT)
poll.poll(2)

# Test select.epoll
print("Testing select.epoll()")
