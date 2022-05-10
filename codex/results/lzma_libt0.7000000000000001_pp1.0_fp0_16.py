import lzma
lzma.open

# This is a hack. We know how to decompress the data, but we don't have a
# file-like object that supports seek(), so we have to load the whole thing
# into memory.
with lzma.open('./big.txt.xz', 'rb') as f:
    data = f.read()

# Now that we have it in memory, we can wrap it into a file-like object.
with io.BytesIO(data) as f:
    # Now we can use the plain vanilla NLTK word_tokenize function.
    print(nltk.word_tokenize(f.read()))
</code>

