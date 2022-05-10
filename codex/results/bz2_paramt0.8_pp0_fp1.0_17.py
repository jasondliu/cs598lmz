from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(open('enwik8', 'rb').read()[:100])

# We have the data we need, but it's in a bytestring.
# We can use the string `decode` method to transform the bytestring into a string object.

#decode the bytestring to a string object
text_string = corpus_file.read()[:100].decode('utf-8')

# There are many different ways of encoding strings as bytes
# We will go over them in the next section.

# Let's now close our file since we don't need it anymore.

#close the file
corpus_file.close()


# ## Closing files
#
# After we have finished reading or writing to a file we need to close it.
#
# This is because computers can only do one thing at a time. While a file
# is open, the computer cannot use that file for something else.
#
# * If we want to reopen the file, we will need to open it again.
# * We may also want to read from or write to other files. We can only do
