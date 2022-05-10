import select
# Test select.select()
# Returns three list of file descriptors that are ready.
# First list is for read events.
# Second list is for write events.
# Third list is for error events.
# If the timeout is specified as 0, it returns three empty lists.

# If the timeout is specified as None, it blocks indefinitely until an event is ready.
print("select.select([sys.stdin], [], [], 0.0):")
print(select.select([sys.stdin], [], [], 0.0))

# If the timeout is specified as a number, it returns three lists after the specified time.
print("select.select([sys.stdin], [], [], 5.0):")
print(select.select([sys.stdin], [], [], 5.0))

# If the timeout is specified as 0, it returns three empty lists.
print("select.select([sys.stdin], [], [], 0.0):")
print(select.select([sys.stdin], [], [], 0.0))


# Test select.poll()
# Returns a list of tuples (
