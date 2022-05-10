import lzma
lzma_file = lzma.LZMAFile('/home/martin/Desktop/moby_dick.txt.xz')

# Now, let's see how long it takes to read the entire file at once:
import time
start = time.time()
lzma_data = lzma_file.read()
end = time.time()

print('READ: {0:.2f} seconds'.format(end - start))

# Now, let's see how long it takes to read the entire file line by line:
start = time.time()
lzma_lines = lzma_file.readlines()
end = time.time()

print('READ LINES: {0:.2f} seconds'.format(end - start))

# Now, let's see how long it takes to read the entire file line by line
# into a list of lines:
start = time.time()
lzma_list = list(lzma_file)
end = time.time()

print('LIST: {0:.2f} seconds'.format(end -
