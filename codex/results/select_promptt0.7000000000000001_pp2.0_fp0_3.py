import select
# Test select.select()
print("select.select():")
r_list, w_list, x_list = select.select([sys.stdin], [], [], 1)
if r_list:
    print("Data available")
else:
    print("No data available")
# Test select.poll()
print("\nselect.poll():")
p = select.poll()
p.register(sys.stdin, select.POLLIN)
p.register(sys.stdout, select.POLLOUT)
print("waiting for events...")
while True:
    events = p.poll(1000)
    for fd, event in events:
        if event & select.POLLIN:
            print("\tstdin is readable")
        if event & select.POLLOUT:
            print("\tstdout is writable")
        if event & select.POLLERR:
            print("\tERROR")

# Test select.epoll()
print("\nselect.epoll():")
e = select.epoll()
print("Type of e:", type(e))
