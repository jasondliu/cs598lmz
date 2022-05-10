import bz2
bz2.BZ2File('compressed_file.bz2', 'wb').write(open('some_file.txt', 'rb').read())
</code>

