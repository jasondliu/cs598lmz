import bz2
bz2.decompress(compressed)

print(compressed)
print(bz2.decompress(compressed))



# with open('C:/Users/mulcas4/AppData/Local/Continuum/anaconda3/envs/python_course/compressed_data.bz2', 'rb') as f:
#     decompressed_data=bz2.decompress(f.read())
#     print(decompressed_data)


with bz2.BZ2File('C:/Users/mulcas4/AppData/Local/Continuum/anaconda3/envs/python_course/compressed_data.bz2') as f:
    file_content=f.read()
    print(file_content)

with gzip.open('C:/Users/mulcas4/AppData/Local/Continuum/anaconda3/envs/python_course/compressed_data.gz', 'rb') as f:
    file_content=f.read()
    print(file_content)

with gzip.open('
