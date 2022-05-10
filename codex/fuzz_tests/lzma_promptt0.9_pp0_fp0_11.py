import lzma
# Test LZMADecompressor.
decompressor = lzma.LZMADecompressor()

while True:
    x = input_file.read(1024)
    if not x:
        break
    y = decompressor.decompress(x)
    if y:
        output_file.write(y)

output_file.writelines(decompressor.unused_data)
output_file.close()

# Python 3.3+:
with lzma.open(path) as input_file:
    with open(output_path, 'wb') as output_file:
        while True:
            chunk = input_file.read(1024)
            if not chunk:
                break
            output_file.write(chunk)

# Python 3.0 - 3.2:
with lzma.LZMAFile(path) as input_file:
    with open(output_path, 'wb') as output_file:
        while True:
            chunk = input_file.read(1024)
            if not chunk:
                break
            output_file.write(
