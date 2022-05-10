import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
I expected shouldn't return any exception, but return empty list,but it show exception:
OSError: [Errno 22] Invalid argument
if i change f.truncate() to m.resize(1), it should okay, but i don't understand why it happen.
thanks


A:

You may be misunderstanding the purpose of truncate. It doesn't remove data, it pads the file with 0s up to the specified size. Therefore you can continue to access the file up to the new size, however any data after the new size will always be 0. What you are trying to accomplish is impossible. You cannot seek beyond the end of the file, and you cannot mmap anything but the entire file.

