from lzma import LZMADecompressor
LZMADecompressor().decompress(data)
</code>
This returns <code>b'PK\x03\x04\x14\x00\x08\x00\x08\x00\t!\x08\xb1\x01\x00\x00\x91\x01\x00\x00\x00\x00'</code>
How to get actual xlsx file without any losses?
I also tried to use <code>xlsxwriter</code> but it doesn't support writing to zip file.
<code>import xlsxwriter
workbook = xlsxwriter.Workbook('test.xlsx', {'constant_memory': True})
worksheet = workbook.add_worksheet()
workbook.close()
</code>
The error I get:
<blockquote>
<p>Traceback (most recent call last):
    File "test.py", line 4, in 
      workbook = xlsxwriter.Workbook('test.xlsx', {'constant_memory': True})
    File "/usr/local/lib/
