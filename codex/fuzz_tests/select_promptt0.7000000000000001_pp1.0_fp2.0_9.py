import select
# Test select.select() with a timeout

timeout = 0.01

readable, writable, exceptional = select.select([sys.stdin], [], [], timeout)
if readable:
    print("Something was read within %s seconds." % timeout)
else:
    print("Nothing was read within %s seconds." % timeout)
