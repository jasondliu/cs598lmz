import select
# Test select.select()

import select
import os
import time

# Create pipes
r, w = os.pipe() 

read_fds = [r]

# Only checking r
# If anything is written to r, put it in write_fds
write_fds, error_fds = select.select(read_fds, [], [])

for f in write_fds:
    data = os.read(f, 1)
    print(data)
    

# Write 5 'a's to the pipe
for x in range(0, 5):
    os.write(w, b'a')

# Select returns the selected file descriptors
read_fds = [r]
write_fds, error_fds = select.select(read_fds, [], [])

for f in write_fds:
    data = os.read(f, 1)
    print(data)
    
print('\nAfter 5 seconds, something is written to the pipe:')

# Sleep 5 seconds before writing to pipe
time.sleep(5)
