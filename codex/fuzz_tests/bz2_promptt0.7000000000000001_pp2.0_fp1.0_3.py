import bz2
# Test BZ2Decompressor for data corruption

filename = 'Moby-Dick.txt.bz2'
filename2 = 'Moby-Dick.txt'

# with bz2.open(filename, 'rb') as input:
#     with open(filename2, 'wb') as output:
#         try:
#             output.write(input.read())
#         except IOError as e:
#             print(e)

with open(filename2, encoding='utf-8') as f:
    text = f.read()

num_characters = len(text)
print('{:,} total characters'.format(num_characters))
num_unique = len(set(text))
print('{:,} unique'.format(num_unique))

sorted_chars = sorted(set(text))
counts = {c: text.count(c) for c in sorted_chars}
print(counts)

# Create a dictionary of all characters
dictionary = dict(zip(sorted_chars, range(len(sorted_chars))))
print("dictionary:", dictionary)
