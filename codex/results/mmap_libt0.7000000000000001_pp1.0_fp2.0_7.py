import mmap

# Create an empty file
# to support a buffering
# protocol
temp_file = NamedTemporaryFile(mode='w+')  # unbuffered
temp_file.write('qqq')
temp_file.seek(0)
print('tempfile:', temp_file.read())

# Create a buffered
# protocol
mapped = mmap.mmap(-1, 3)
mapped.write('www')

print('mapped:', mapped)
print('mapped:', mapped[:])  # read

print('mapped:', mapped.find('w'))  # search

mapped.seek(0)

print('mapped:', mapped.readline())

print('mapped:', mapped.readline())

print('mapped:', mapped.readline())

mapped.close()

mapped = mmap.mmap(-1, 3)
mapped.write('www')

print('mapped:', mapped)
print('mapped:', mapped[:])  # read

print('mapped:', mapped.
