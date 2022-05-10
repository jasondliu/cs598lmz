import mmap
# Test mmap.mmap.RESERVE_FILE
with open('tests/resources/bar', 'rb') as f:
    m = mmap.mmap(f.fileno(), 0, mmap.mmap.RESERVE_FILE)
    m.close()

# Test os.sep on Windows
if sys.platform == "win32":
    assert '\\' == os.sep

# Test os.stderr has no bufferings
assert 0 == os.stderr.write('abc')

# Test os.stdout has bufferings
assert len('abc') == os.stdout.write('abc')

# Test os.system
assert 0 == os.system('exit 0')

# Test os.uname
assert len(os.uname()) == 5

# Test os.utime
t = time.time()
os.utime('tests/resources/foo', None)
assert py.test.raises(OSError, os.utime, 'does-not-exist', (t,t))

