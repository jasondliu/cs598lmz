import select
# Test select.select

# We need to poll the StdIn file descriptor
# We can use select.select in this case because its the only fd thats
# being polled

# Check if StdIn is ready for reading
print(select.select([sys.stdin], [], [], 0))

# Check if StdIn is ready for reading
# Change the timeout to 10 seconds and then input any text
# on the terminal
print(select.select([sys.stdin], [], [], 10))
# Wait for 10 seconds and the input any text
# The third list is for error codes

# If select returns an empty list, then there is an error
# Read from sys.stdin

reason = select.select([sys.stdin], [], [])[0][0].read()
