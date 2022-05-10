import select
# Test select.select
print("select.select:")
for i in range(10):
    readable, writable, exceptional = select.select([sys.stdin], [], [], 1)
    if readable:
        s = sys.stdin.readline()
        print("You said", s)
    else:
        print(i+1, "seconds elapsed")

# Test select.poll
print("\nselect.poll:")
# Set up the poller
poll_object = select.poll()
poll_object.register(sys.stdin, select.POLLIN)
# Poll for 10 seconds
for i in range(10):
    events = poll_object.poll(1000)
    if events:
        s = sys.stdin.readline()
        print("You said", s)
    else:
        print(i+1, "seconds elapsed")

# Test select.epoll
print("\nselect.epoll:")
# Set up the epoller
epoll_object = select.epoll()
epoll_object.register(sys.stdin.fileno(), select
