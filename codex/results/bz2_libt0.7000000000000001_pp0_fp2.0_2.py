import bz2
bz2.decompress(bz2_data)

# 2. bz2.compress()

bz2_data = bz2.compress(original_data)

# 3. bz2.open()

bz2_file = bz2.open(bz2_filename, mode='wt')
bz2_file.write(original_data)
bz2_file.close()
 
# 4. bz2.BZ2File()

bz2_file = bz2.BZ2File(bz2_filename, mode='wt')
bz2_file.write(original_data)
bz2_file.close()

# 5. bz2.open() in read mode

bz2_data = bz2.open(bz2_filename, mode='rt').read()
print(bz2_data)

# 6. bz2.BZ2File() in read mode

bz2_file = bz2.BZ2File(bz2_filename, mode='rt
