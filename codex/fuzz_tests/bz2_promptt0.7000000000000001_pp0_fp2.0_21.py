import bz2
# Test BZ2Decompressor

bz2decompressor = bz2.BZ2Decompressor()

with open('../data/dna.example.fasta.bz2', 'rb') as dnafile:
    dnastring = dnafile.readline().decode()
    dnastring += bz2decompressor.decompress(dnafile.read()).decode()
    dnastring = dnastring.rstrip()

print(len(dnastring))
print(dnastring.count('A'))
print(dnastring.count('C'))
print(dnastring.count('G'))
print(dnastring.count('T'))

# Expected output
# 149996
# 39087
# 38119
# 39717
# 37173

# This one is a bit more tricky. We need to iteratively decompress the data in a loop.

with open('../data/dna.example.fasta.bz2', 'rb') as dnafile:
    dnastring
