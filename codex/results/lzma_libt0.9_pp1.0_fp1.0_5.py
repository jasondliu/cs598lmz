import lzma
lzma_out = lzma.compress(json.dumps(tree1).encode(), preset=9)
print(len(lzma_out))
with open('tree1.lzma', 'wb') as fh:
    fh.write(lzma_out)
with open('tree1.lzma', 'rb') as fh:
    lzma_data = fh.read()
data7 = json.loads(lzma.decompress(lzma_data).decode())
assert_equal(data7, tree1)
 

print('Done!')
