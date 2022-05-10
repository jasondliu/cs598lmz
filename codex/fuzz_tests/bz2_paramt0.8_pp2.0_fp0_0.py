from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(bz2_compressed_file)
</code>
but <code>BZ2Decompressor().decompress(bz2_compressed_file)</code> returns <code>bytes</code> and I can't use it with <code>shutil.copyfileobj()</code> because I get <code>TypeError: argument should be string or read-only character buffer, not bytes</code>
I'm on Python 3.7, so the question is how to convert the output to <code>string</code> or <code>read-only character buffer</code> so I can feed it to <code>shutil.copyfileobj()</code> like I'm doing in my code
Here is how I'm getting <code>bz2_compressed_file</code>:
<code>bz2_compressed_file = ftp.retrbinary("RETR " + file_name, self.__write_to_file)
</code>
and <code>__write_to_file</code> is
<code>def __write_to_file(self, chunk):

