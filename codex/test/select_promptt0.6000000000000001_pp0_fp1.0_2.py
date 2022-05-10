import select
# Test select.select()
# See http://docs.python.org/library/select.html

# Note: 
#   select.select() works on Windows, but not on Linux.
#   select.poll() should be used instead on Linux.

# Set up the data structures for polling
inputs = [ sys.stdin ]
outputs = [ ]
