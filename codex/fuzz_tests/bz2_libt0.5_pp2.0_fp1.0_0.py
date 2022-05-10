import bz2
bz2_decompressor = bz2.BZ2Decompressor()

with gzip.GzipFile('file_path') as gzfile:
    with bz2.BZ2File('file_path') as bzfile:
        for line in gzfile:
            # Do something with line
        for line in bzfile:
            # Do something with line
</code>

