import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]

print('done')
</code>
In Python 3.3, it prints <code>done</code> as expected.
In Python 3.2, it prints <code>ValueError: mmap length is zero</code>.
Is this new behaviour a bug or a feature?


A:

For the sake of tracking this down, the bug is fixed in commit 9bd3977c2b2e.
This change was introduced in Python 3.3 beta 1, and the relevant commit message is:
<code>Misc

- Fix a bug in mmap.mmap() which caused a crash when a file is truncated
  after the mmap object is created. Patch by Antoine Pitrou. Closes #16096.
  Patch by Stefan Krah. Closes #16594.

- Fix objc.pyobjc_id() so it works with subclasses of built-in types.
  Patch by Ronald Oussoren. Closes #17182.
</code>
So, it seems this is intentional, and not a bug.

