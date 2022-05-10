import lzma
lzma.LZMAError: Not enough data for header
</code>
It is a huge file, nearly 1GB.
I have tried to use the <code>lzma</code> module directly, but it does not work well.
I have also tried to use <code>lzma.LZMAFile</code> but it also does not solve the problem.
My Python version is 3.8.2.
Here is my code:
<code>import tarfile
import lzma

tar = tarfile.open('test.tar.lzma', 'r')
tar.extractall()
tar.close()
</code>


A:

Try this:
<code>import tarfile

tar = tarfile.open('test.tar.lzma', 'r:xz')
tar.extractall()
tar.close()
</code>

