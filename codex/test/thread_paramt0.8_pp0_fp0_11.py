import sys, threading
threading.Thread(target=lambda: sys.stdout.write('stuff\n')).start()

# 3.2
while True:
    sys.stdout.write('stuff\n')
    i = input('Type something: ')
    print('Foo bar.')
# write
# write
# read
# write
# write

# 3.3
# No, there isn't enough information. There is no way to be sure whether the
# write was actually handled by the underlying network socket.

# 3.4
import sys, select
for i in range(5):
    sys.stdout.write('stuff\n')
    select.select([sys.stdin], [], [], 0)
# stuff
# stuff
# stuff
# stuff
# stuff

# 3.5
import sys
for i in range(5):
    sys.stdout.write('stuff\n')
    sys.stdout.flush()
# stuff
# stuff
# stuff
# stuff
# stuff

# 3.6
while True:
    sys.stdout.write('stuff\n')
    sys.std
