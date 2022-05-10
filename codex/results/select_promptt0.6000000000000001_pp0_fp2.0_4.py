import select
# Test select.select()
#
# select(): 
#   1. Waiting for I/O completion on multiple streams
#   2. Monitoring multiple streams for activity
#   3. Implementing timeouts and deadlines in network clients
#   4. Implementing asynchronous I/O in network clients
#

# The select() function takes three lists of streams as input, and returns 
# lists of subsets of those same streams as output. 
#
# The first list passed to select() is a list of streams to check for readability.
# The second list is a list of streams to check for writability.
# The third list is for streams to check for errors.
#
# The return value is a three-item tuple containing three lists of stream objects:
#   - readable: streams that have data available for reading
#   - writable: streams that can be written to without blocking
#   - exceptional: streams with errors pending
#
# If the timeout expires before any streams are ready, the three tuples will be empty.
# If the timeout is omitted, select() blocks indefinitely until at least one stream is ready.
# If a timeout is given and expires before
