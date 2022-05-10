import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]    
    m.close()
    print(a)

os.remove('test')
</code>
The output would be <code>[0]</code>, since the file was truncated, but the data in the memory mapping was not. Is it possible to safely "sync" the memory mapping with the file? Or perhaps there's a way to handle the <code>mmap.error</code> exception, that's happening now?

