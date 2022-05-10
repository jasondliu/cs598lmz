import mmap
# Test mmap.mmap
# my_file = open('./test_mmap.txt', 'w')
# my_file.write('Hello Python!\n')
# my_file.close()
#
# mm = mmap.mmap(my_file.fileno(), 0)
# print(mm.readline())
# print(mm.readline())


# Test mmap.mmap with binary file
# mm = mmap.mmap(-1, 13)
# # mm.write(b'Hello Python!\n')
# print(mm.read(13))
# mm.seek(0)
# print(mm.read(13))
# mm.close()

# Test mmap.mmap with string
# mm = mmap.mmap(-1, 13)
# mm.write(b'Hello Python!\n')
#
# # Move to the beginning
# mm.seek(0)
#
# # Read the entire content of the mmap object
# print(mm.readline())
#
# # Close the mmap object
# mm.close()

# Test
