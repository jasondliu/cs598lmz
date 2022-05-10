import lzma
# Test LZMADecompressor
# Parses a directory and performs compression on each file.
# Files have to have less than 4GB to be compressed.
#
class NotABinaryFile(Exception): pass

class LZMANotABinaryFile(NotABinaryFile): pass

def compress_file(file_name):
    try:
        with open(file_name, 'rb') as file:
            content = file.read()
        lzma_content = lzma.compress(content)
        space_saving = (1 - len(lzma_content) / len(content)) * 100
    except NotABinaryFile:
        return

    new_file_name = file_name + '.xz'
    print('{:2f}% space save by compressing {}'.format(space_saving, file_name))
    with open(new_file_name, 'wb') as fp:
        fp.write(lzma_content)
    return new_file_name


