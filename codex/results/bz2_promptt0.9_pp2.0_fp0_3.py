import bz2
# Test BZ2Decompressor
# https://docs.python.org/3/library/bz2.html

path = "/Users/chloe/Documents/2017-18/teaching/paws_2018/unit_tests/use_link_page_3.xml.bz2"

f = bz2.open(path, 'rb')

chunk_size = 10 ** 4

dc = bz2.BZ2Decompressor()
done = False
data = b''
while not done:
  new_data = f.read(chunk_size)
  if len(new_data) == 0:
    # finished reading BZ2 data
    done = True
  else:
    # add read data to decompression buffer
    decompressed_data = dc.decompress(new_data)

    # reset buffer to concatenate decompressed data
    data = b''
    data += decompressed_data
#     print(data)


print(len(data))
print(data[:1000])

# Test BZ2File for reading

# https://docs.python.org
