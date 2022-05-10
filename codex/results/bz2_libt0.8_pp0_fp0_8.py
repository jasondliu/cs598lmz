import bz2
bz2.compress(data)

def progress(blocks, block_size, total_size):
    current = blocks*block_size
    print '\r %.2f%%' % (100.0 * current/total_size),
    sys.stdout.flush()

urllib.urlretrieve('http://www.python.org', 'python.html', reporthook=progress)
