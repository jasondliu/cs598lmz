import select
# Test select.select()
print('Waiting for reads on more than one FD:')
read_set, write_set, e_set = select.select([sys.stdin, sys.stdout], [], [])
print('Reads:', read_set)
print('Writes:', write_set)
print('Exceptions:', e_set)
print('... done')
# Raw I/O
class raw_fmt(object):
    def read(self, size):        
        if size > sys.maxsize:
            size = sys.maxsize
        result = os.read(self.fd, size)
        if len(result) == 0:
            raise EOFError
        return result
    def write(self, data):
        return os.write(self.fd, data)
    def close(self):
        try:
            fd = self.fd
        except AttributeError:
            pass
        else:
            os.close(fd)
            del self.fd
f = open('/dev/tty', 'r+', 0)      # open tty in raw mode
