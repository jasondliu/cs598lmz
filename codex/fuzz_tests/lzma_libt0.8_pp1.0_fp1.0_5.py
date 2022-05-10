import lzma
lzma.LZMA_FORMAT_RAW = 3

print('\nstart\n')

f_input = open('input/ru_RU_6.0.6_0/bundles/ru_RU.dic', 'rb')
f_output = open('output/ru_RU_6.0.6_0.dic', 'wb')

print('read bundle data')
data = f_input.read()
f_input.close()

print('decompress bundle data')
decompressed_data = lzma.LZMADecompressor().decompress(data)

print('write decompressed bundle data')
f_output.write(decompressed_data)
f_output.close()

print('end\n')
