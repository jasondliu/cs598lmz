import select
# Test select.select for edge triggered mode
print 'Edge triggered test:'
import fcntl
print 'with old flg fcntl.fcntl(fd, fcntl.F_GETFL): ', fcntl.fcntl(sys.stdin.fileno(), fcntl.F_GETFL)
fcntl.fcntl(sys.stdin.fileno(), fcntl.F_SETFL, os.O_NONBLOCK)
print 'with new flg fcntl.fcntl(fd, fcntl.F_GETFL): ', fcntl.fcntl(sys.stdin.fileno(), fcntl.F_GETFL)
inputs = [sys.stdin]
timeout = 5
print 'inputs li
