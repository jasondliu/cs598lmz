import bz2
bz2.decompress(bz2_data)

# bz2.decompress(bz2_data)
# TypeError: a bytes-like object is required, not 'str'

# bz2.decompress(bz2_data.encode())
# TypeError: argument should be a bytes or a file object

# bz2.decompress(bz2_data.encode()).decode()
# TypeError: argument should be a bytes or a file object

# bz2.decompress(bz2_data.encode()).decode('utf-8')
# TypeError: argument should be a bytes or a file object

# bz2.decompress(bz2_data.encode('utf-8'))
# TypeError: argument should be a bytes or a file object

# bz2.decompress(bz2_data.encode('utf-8')).decode()
# TypeError: argument should be a bytes or a file object

# bz2.decompress(bz2_
