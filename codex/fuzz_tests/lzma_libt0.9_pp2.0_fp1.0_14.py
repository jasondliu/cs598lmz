import lzma
lzma.decompress(test4_raw)

# if the destination is a file, the LZMA file is unpacked to the destination
print('Testing unpacking to a file...')
test1_dest = '.testfile_unpack_to_file_1'
test2_dest = '.testfile_unpack_to_file_2'
test3_dest = '.testfile_unpack_to_file_3'

file_context = BytesIO(test1_raw)
file_to = BytesIO()
unpack_lzma_file(file_context, file_to)
assert equal_files(test1_dest, file_to), 'Error unpacking to a file...'

file_context = BytesIO(test2_raw)
file_to = BytesIO()
unpack_lzma_file(file_context, file_to)
assert equal_files(test2_dest, file_to), 'Error unpacking to a file...'

file_context = BytesIO(test3_raw)
file_to = BytesIO
