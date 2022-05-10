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
gc.collect()
</code>
Output on Python 3.7.2:
<code>% python3 /tmp/t.py 
102
% python3 /tmp/t.py 
102
% python3 /tmp/t.py 
102
% python3 /tmp/t.py 
102
% python3 /tmp/t.py 
102
% python3 /tmp/t.py 
102
% python3 /tmp/t.py 
102
% python3 /tmp/t.py 
102
% python3 /tmp/t.py 
102
% python3 /tmp/t.py 
102
% python3 /tmp/t.py 
102
% python3 /tmp/t.py 
102
% python3 /tmp/t.py 
102
% python3 /tmp/t.py 
102
% python3 /tmp/t.py 
102
% python3 /tmp/t.py 
102
% python3 /tmp/t.py 
102
% python3 /tmp/t.py 

