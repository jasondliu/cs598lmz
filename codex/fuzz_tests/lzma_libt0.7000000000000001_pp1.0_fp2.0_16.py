import lzma
lzma_obj = lzma.LZMAFile('test.xz', 'w')  # or BZ2File
lzma_obj.write(original_data)
lzma_obj.close()

lzma_obj = lzma.LZMAFile('test.xz', 'r')  # or BZ2File
data = lzma_obj.read()
lzma_obj.close()

print(data)
print(original_data)
</code>

