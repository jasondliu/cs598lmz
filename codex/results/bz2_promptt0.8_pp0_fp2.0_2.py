import bz2
# Test BZ2Decompressor
decompressor = bz2.BZ2Decompressor()
with open('to_decompress.bz2') as f_input, open('to_decompress.out', 'wb') as f_output:
    decompressor.decompress(f_input.read(), f_output)
with open("to_decompress.out") as f_input:
    print("\n".join(f_input.readlines()))

# Test BZ2File
with bz2.open("to_decompress.bz2", "r") as f_input:
    print("\n".join(f_input.readlines()))

# Test bz2.decompress
with open("to_decompress.bz2", "rb") as f_input:
    data = f_input.readlines()
    for line in data:
        print(bz2.decompress(line))
