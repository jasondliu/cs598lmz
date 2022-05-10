import bz2
bz2.compress(open('the.tar', 'rb').read())
</code>
and the bz2 lib works fine.
Thanks


A:

Call tarfile.TarFile.add(filename) or tarfile.TarFile.addfile(tarinfo) to add members to an existing tarfile.  Call tarfile.TarFile.close() or tarfile.TarFile.flush() to write the data to the file.
The flush() method will write the archive to a file object, such as an open file or a StringIO:
<code>tar = tarfile.open(filename)
tarfile.add(fname)
tarfile.addfile(tarinfo)
...
import StringIO
tar.flush(StringIO.StringIO())
</code>

