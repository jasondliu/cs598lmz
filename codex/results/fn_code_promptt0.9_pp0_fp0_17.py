fn = lambda: None
# Test fn.__code__.co_filename a few times and make sure the same run always
# returns the same result.
filenames: Set[str] = set()
for _ in range(5):
    code = TestCompile.__code__.co_filename
    filenames.add(code)

assert len(filenames) == 1
assert filenames.pop() == 'TestCompile.py'

# Test if filename is always 'test_misc'
app = TestApp()
code = app.__code__.co_filename
assert code == 'test_misc'

# Test if __name__ can be overwritten
subdir = os.path.dirname(__file__)
os.chdir(subdir)
python = sys.executable

try:
    # __name__ can be overwritten by the script
    args = [python, 'nonexistent.py']
    res = check_subprocess(args, 'stdout', 'stderr')
    assert res.returncode == 0
    assert res.stdout == b''
    assert res.stderr ==
