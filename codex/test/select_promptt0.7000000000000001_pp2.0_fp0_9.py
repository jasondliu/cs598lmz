import select
# Test select.select() by selecting stdin
import sys
print('Press a key within 5 seconds ...')
r, w, x = select.select([sys.stdin], [], [], 5)
if r:
    print('You pressed', sys.stdin.readline().rstrip())
else:
    print('Time up!')

# Test select.poll() by selecting stdin
import select
import sys
print('Press a key within 5 seconds ...')
p = select.poll()
