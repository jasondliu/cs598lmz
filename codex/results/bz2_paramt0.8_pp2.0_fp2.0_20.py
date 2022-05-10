from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(bz2.read(bz2_file_name))

if __name__ == '__main__':
  a = get_matrix_hardcoded()
  b = get_matrix_csv()
  c = get_matrix_bz2()
