import bz2
bz2_file = bz2.BZ2File(bz2_file_name)
data = bz2_file.read()
bz2_file.close()

# uncompress the data
uncompressed_data = bz2.decompress(data)

# write the data to a file
dst_file = open(dst_file_name, 'wb')
dst_file.write(uncompressed_data)
dst_file.close()
</code>

