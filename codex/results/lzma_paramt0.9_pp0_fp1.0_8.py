from lzma import LZMADecompressor
LZMADecompressor()

def append_vcf(file_list, output_file_path, sample_name, mode=0o755):
    outfile = output_file_path
    for fname in file_list:
        outfile.write('\n')
        outfile.write('#######')
        outfile.write('\n')
        outfile.write((fname.split('/'))[-1]+'\n')
        with open(fname, 'r') as infile:
            outfile.write(infile.read())


def compress_vcf(w_file):
    compress_obj = LZMADecompressor()
    temp_path = write_command.get(w_file._file_id)
    with open(temp_path.name, 'rb') as w:
        infile = w
    with open(w_file.name, 'wb') as f:
        with open(temp_path.name, 'rb') as temp:
            for line in infile:
                line = line
                if not line.startswith(b
