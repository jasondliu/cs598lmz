import io

class File(io.RawIOBase):
    def readinto(self, buf):
        global view
        view = buf
    def readable(self):
        return True

f = io.BufferedReader(File())
f.read(1)
del f
</code>
I don't do any reference counting, but if I understood the issue with the previous code well, because I used a CPython myself, so there is no question about what I do. I do the same in PyPy.
And, then I use the <code>view</code> to display some info in a worker thread, which runs through Sqlite3 operations:
<code>global view
ftime = None
while True:
    try:
        time.sleep(interval)
        fview = open('/dev/shm/finder_view', 'wb')
        fview.write(view)
        fview.close()
    except OSError as e:
        if 'No such file' in e.strerror:
            if ftime is None:
                ftime = time.time()
            if time.time() - ftime &gt; 10:
                print('no file')
                sys.exit()
        else:
            raise
    else:
        ftime = None
</code>
The above code is not (yet?) part of the C extension, but it
