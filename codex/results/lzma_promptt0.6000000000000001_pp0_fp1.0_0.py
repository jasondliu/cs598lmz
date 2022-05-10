import lzma
# Test LZMADecompressor class
# https://docs.python.org/3/library/lzma.html

with lzma.open('enwik8') as f:
    file_content = f.read()
    print(file_content[:100])

decompressor = lzma.LZMADecompressor()
result = decompressor.decompress(file_content)
print(result[:100])

# Now we have the decompressed data
# We need to turn back into a list of words
# For that, we will use the split function

# the split function will split a string into a list of strings
# depending on the character we put in the ()
# https://docs.python.org/3/library/stdtypes.html#str.split

# Example

my_string = "Hi! My name is Pedro and I love Python"
my_string.split(" ")

# split will return a list of strings
# if we want to keep the punctuation, we need to include it in the list

my_string.split(" ")

# We want the punctuation
