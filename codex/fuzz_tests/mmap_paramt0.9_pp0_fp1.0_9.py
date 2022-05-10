import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    # --- add 'r' or 'w' here as well in the line below
    mprot = mmap.ACCESS_READ | mmap.ACCESS_WRITE
    m.resize(100, mprot)
    print('file size:', os.stat('test').st_size)
</code>
Initial size:
<code>$ ll -h test
1 -rw-rw-r--  1 sschaef  staff   0B 11 Mar  1:38 test
</code>
New size:
<code>$ python3 resize_file.py
file size: 100

$ ll -h test
1 -rw-rw-r--  1 sschaef  staff   0B 11 Mar  1:39 test
</code>

