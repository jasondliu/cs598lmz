import lzma
lzma.decompress(codecs.decode(''.join(in_list), 'hex'))

# -> 'witch which has which witches wrist watch'
