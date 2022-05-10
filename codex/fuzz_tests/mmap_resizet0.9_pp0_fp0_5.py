import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]

print(a)

os.remove('test')
</code>
This is because the mmap object isn't updated when the file is truncated.  See this bug report for the original description.
There doesn't appear to be a documented way to force an update of the mmap object after the file is changed.
So in the above example, mmap will throw an exception since the file has been truncated.  I'm wondering if there is a way to force mmap to update itself when a file is truncated like this?

