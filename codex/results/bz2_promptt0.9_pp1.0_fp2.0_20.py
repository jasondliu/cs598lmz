import bz2
# Test BZ2Decompressor object

dec = bz2.BZ2Decompressor()

comp_data = open('./files/sample.bz2', 'rb').read()
decomp_data = []
temp = None

for part in comp_data:
    temp = dec.decompress(part)
    if temp:
        decomp_data.append(temp)

print(decomp_data[:10]) # Bytes
print(b''.join(decomp_data)[:100]) # Bytes

# as string:
print(b''.join(decomp_data).decode()[:100])

# Write to file
print("Writing file...")
with open('./files/sample2.txt', 'w') as f:
    f.write(b''.join(decomp_data).decode())
    
print("done.")

# Compress again
print("Compressing again...")
compressed = bz2.compress(b''.join(decomp_data))
print("done.")

# Is it the same?
print("Are they the same?
