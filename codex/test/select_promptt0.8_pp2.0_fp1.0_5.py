import select
# Test select.select on sockets with no I/O

# Try to create a socket in each possible state, and call select() on it
# to see if it reports any readiness.

