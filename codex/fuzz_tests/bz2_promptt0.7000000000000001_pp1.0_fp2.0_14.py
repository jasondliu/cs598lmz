import bz2
# Test BZ2Decompressor to decompress bz2 file
with bz2.BZ2File("enwiki-latest-pages-articles.xml.bz2", "r") as bz2_file:
    decompressor = bz2.decompress(bz2_file.read())
# With BZ2Decompressor
decompressor = bz2.BZ2Decompressor()
with gzip.GzipFile("enwiki-latest-pages-articles.xml.bz2", "r") as gzip_file:
    file_content = gzip_file.read()
    while file_content:
        decompressed_data = decompressor.decompress(file_content)
        if decompressed_data:
            print(decompressed_data)
        file_content = gzip_file.read()

# With decompress
with gzip.GzipFile("enwiki-latest-pages-articles.xml.bz2", "r") as gzip_file:
    file_content = gzip_file.read()
    while file_content:
        decompressed_data
