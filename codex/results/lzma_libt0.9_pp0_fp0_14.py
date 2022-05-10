import lzma
lzma.decompress(line).decode()

def decompress(file_name, out_dir):
    """To decompress a lzma file to text file."""
    with open(file_name, 'rb') as input, open(out_dir, 'w') as output:
        try:
            output.write(lzma.decompress(input.read()).decode())
        except OSError:
            print("Error: Wrong compression format. Must be .xz or .lzma")

output_file_name1 = path_to_lzma_files + 'wiki-trec'
decompress(file_name, output_file_name1)
with open(output_file_name1, 'r') as input:
    for line in input.readlines()[:100]:
        print(line)

from smart_open import smart_open

file_name = path_to_lzma_files + 'wiki-trec-jfs.txt.lzma'
reader = smart_open.smart_open(file_
