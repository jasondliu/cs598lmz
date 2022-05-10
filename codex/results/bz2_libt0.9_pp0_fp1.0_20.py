import bz2
bz2.BZ2Compressor()
</code>
But also remember that if you are using python version smaller than 2.3, you need to define a <code>compress</code> method:
<code>class NullCompressor:
    def compress(self, input):
        return input

compressor = NullCompressor()
internal_archive = BytesIO()
with tarfile.TarFile(fileobj=internal_archive, mode="w",
                     format=tarfile.PAX_FORMAT,
                     compress=1) as archive:
    for myfile in files:
        archive.add(myfile)
</code>
I tested both approaches with Python 2.7.

