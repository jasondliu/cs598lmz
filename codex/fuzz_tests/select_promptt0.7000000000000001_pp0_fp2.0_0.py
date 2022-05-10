import select
# Test select.select
import time

def write():
    for i in range(5):
        print('write %d' % i)
        time.sleep(1)

def read():
    for i in range(5):
        print('read %d' % i)
        time.sleep(1)

read_fd, write_fd = os.pipe()

rw_fd, _, _ = select.select([read_fd], [write_fd], [])

# Fork returns twice, once for parent, once for child.
pid = os.fork()

if pid < 0:
    print('fork failed')
elif pid == 0:
    # in child
    os.close(write_fd)
    read()
    os.close(read_fd)
    print('child exiting')
else:
    # in parent
    os.close(read_fd)
    write()
    os.close(write_fd)
    print('parent exiting')
