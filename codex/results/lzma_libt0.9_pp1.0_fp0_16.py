import lzma
lzmaCompressFile()
</code>
I'm getting this error:
<code>Traceback (most recent call last):
  File "C:\Users\Miraz\Desktop\compressTEST.py", line 8, in &lt;module&gt;
    lzmaCompressFile()
  File "C:\Users\Miraz\Desktop\compressTEST.py", line 5, in lzmaCompressFile
    data = open("C:\\Users\\Miraz\\Documents\\FSR.txt", "rb").read()
FileNotFoundError: [Errno 2] No such file or directory: 'C:\\Users\\Miraz\\Documents\\FSR.txt'
</code>
I tried to change the destination path from <code>C:\\</code> to <code>\\</code>.
I also tried to give the full path  like <code>\\Users\\Miraz\\Desktop\\FSR.txt</code>
 but still no luck.
I also added <code>test.py</code> and <code>FSR.txt</code> to the same directory. 

