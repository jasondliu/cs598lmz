import bz2
# Test BZ2Decompressor object
with bz2.BZ2File('test.xml.bz2', 'rb') as xml_file:
        file_content = xml_file.read()

print(len(file_content))

# Test decompressor directly
decompressor = bz2.BZ2Decompressor()
with open('test.xml.bz2', 'rb') as xml_file:
    file_content = xml_file.read()
    unzipped_file = decompressor.decompress(file_content)
    unzipped_file += decompressor.flush()
print(len(unzipped_file))



# Example 2: Using the bz2 module to compress data in memory
import bz2

original_data = b'This is the original text.'
print('Original     : {} bytes'.format(len(original_data)))

compressed = bz2.compress(original_data)
print('Compressed   : {} bytes'.format(len(compressed)))

decompressed = bz2.decompress(compressed)
print('Dec
