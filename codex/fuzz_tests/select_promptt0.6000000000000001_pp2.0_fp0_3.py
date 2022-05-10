import select
# Test select.select() for timeout == 0
import sys
import time

timeout = 0

# Create an empty pipe
r, w = os.pipe()

# Create a select() object
s = select.select([r], [], [], timeout)

# Open the write end of the pipe for writing
w = os.fdopen(w, 'w')

# Write to the pipe
w.write('test')
w.flush()

# Close the write end of the pipe
w.close()

# Wait for a little while before continuing
# This is to allow select() to detect that the pipe is readable
time.sleep(1)

# Check the results
if s != ([r], [], []):
    print "Failed"
else:
    print "Passed"
