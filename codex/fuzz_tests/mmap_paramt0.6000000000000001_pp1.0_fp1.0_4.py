import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    while True:
        m.seek(0)
        print(m.read(1))
        time.sleep(1)
</code>
The problem is that the mmap object is not updated when the file is modified. I can see it with <code>hexdump</code> that the file is indeed modified, but it is not reflected in the mmap object.
<code>$ hexdump test
0000000 00
0000002

$ hexdump test
0000000 00
0000002

$ echo "0" &gt; test

$ hexdump test
0000000 30
0000002

$ hexdump test
0000000 30
0000002

$ echo "1" &gt; test

$ hexdump test
0000000 31
0000002

$ hexdump test
0000000 31
0000002
</code>
I thought that mmap was supposed to be updated automatically (that is the whole point of the <code>MAP_SHARED</code> flag). What am I doing wrong here?

