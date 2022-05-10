import lzma
lzma_file = os.path.join(os.getcwd(), "solved_lzma")
result = lzma.decompress(open(lzma_file, 'rb').read())
print(result.decode())
