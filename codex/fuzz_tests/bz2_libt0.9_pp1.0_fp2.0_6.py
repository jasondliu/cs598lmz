import bz2
bz2_file = bz2.BZ2File(bz2_file, mode= 'r')
uncompressed_string = bz2_file.read()
# TODO: uncompressed string
# uncompressedString is just a string
print(uncompressed_string)

uncompressed_string = uncompressed_string.decode('ascii')
print(uncompressed_string)

text = uncompressed_string.split('\n')
print(text)


# The 'proto' attribute here is the standard Python protocol number that corresponds to the protocol used to pickle the object
# bz2 compresses the file with bz2 protocol
test_text = text[0]
print(test_text)

print('\n','Test Dictionary','\n')

test_dictionary = pickle.loads(test_text)
print(test_dictionary)


# The nested dictionary
# It's not a dictionary
# It's a bunch of different stuff that are pickled
print(type(test_dictionary[0]))
print(test_dictionary[0])
