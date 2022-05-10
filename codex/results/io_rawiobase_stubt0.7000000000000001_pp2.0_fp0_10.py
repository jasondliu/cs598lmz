import io
class File(io.RawIOBase):
    def __init__(self,filename):
        self.file=open(filename,'r')
    def read(self,n):
        return self.file.read(n)
    def close(self):
        self.file.close()
    def seekable(self):
        return True
    def readable(self):
        return True
</code>
and in my python3 script:
<code>import File
import codecs
import csv

reader=codecs.getreader('iso-8859-15')(File.File("test.csv"))
csvreader=csv.reader(reader)
for row in csvreader:
    print(row)
</code>
but it failed with the following error:
<blockquote>
<p>UnicodeDecodeError: 'utf-8' codec can't decode byte 0xcc in position
  115: invalid continuation byte</p>
</blockquote>
Any idea?


A:

<code>codecs.getreader</code> creates a text stream from a file.
You should use <code>codec
