import lzma
# Test LZMADecompressor
decompressor = lzma.LZMADecompressor()
decompressor.decompress(data)
fantasy_zip = zipfile.ZipFile('data/zip.zip')
fantasy_zip.namelist()

one_file = fantasy_zip.open('10001-8.txt')
print(one_file)

example_5 = str(one_file.read())

print(example_5)
 
print(len(example_5))

print(str(example_5)[0:80])

print(len(str(example_5)))

with one_file as file_2:
    example_6 = str(file_2.readlines())
    print(example_6)
    print(len(example_6))
    print(example_6[0:80])
    
one_file.close()
example_5[0:80]
 
assert(type(example_5) is str)

assert(type(example_6) is str)
fantasy_zip.infolist()

one_file
