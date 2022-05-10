import io
class File(io.RawIOBase):
    def __init__(self, url):
        self.url = url
        self.f = open(url, "r")
    def read(self, size=-1):
        return self.f.read(size)
    def readable(self):
        return True
    def seekable(self):
        return True
</code>
and then I can simply use this with the following code :
<code>import ftplib
import io

f = File()
f.write(ftp.retrlines('RETR ' + filename)[-1])
f.seek(0)
df = pd.read_csv(f, delimiter='\t')
</code>
But I am getting the following error :
<blockquote>
<p>PermissionError: [Errno 13] Permission denied</p>
</blockquote>
Is there any alternative or another way to solve this problem?


A:

The error is probably related to ftp connection. You can try:
<code>import ftplib
import io
from ftplib import FTP
import pandas as p
