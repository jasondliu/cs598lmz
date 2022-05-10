import bz2
bz2.decompress(b_stream)
</code>
I also tried : 
<code>zlib.decompress(b_stream, -zlib.MAX_WBITS)
</code>
And I got the same error. Any ideas ?
EDIT
It seems that the data I'm getting is gzipped, not bzipped. So I'm getting this error when I try this : 
<code>with open(file_name, 'rb') as f:
      b_stream = f.read()
      print(b_stream)
      print(zlib.decompress(b_stream))
</code>
The error is : 
<code>Error -3 while decompressing data: incorrect header check
</code>
EDIT 2
It seems that zlib cannot work with the file I'm trying to unzip. Without the header, I cannot use gzip, and I cannot use zlib since it needs one. I saw that there were some gzip libraries for python... Is it possible that that file is not gzipped ? 


A:

I found the answer. The file was indeed gz
