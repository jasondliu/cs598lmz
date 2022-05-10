import bz2
bz2_file = bz2.BZ2File('docs_to_check/movies_awards.txt.bz2', 'rb')
bz2_file.readlines()

Compression ratio is 7.51 to 1, in other words, we get a file that is 7 times smaller in size with the same information
'''

def bz2_compress(file_to_compress, output_file_name, blocksize):
    with open(file_to_compress, 'rb') as in_file:
        with bz2.BZ2File(output_file_name, 'wb', compresslevel=1) as out_file:
            for block in iter(lambda: in_file.read(blocksize * 16 * 1024), b''):
                out_file.write(block)
                print(".", end='')
            print("\nDone...")

def main():
    file_to_compress = "docs_to_check/movies_awards.txt"
    output_file_name = "movies_awards_bz2.
