import lzma
lzma.decompress(b'YWJjZA==')

compress = lzma.compress
decompress = lzma.decompress
compress_level = 9

compress_func = compress
decompress_func = decompress

compress_to_file = lzma.compress
decompress_from_file = lzma.decompress
compress_file_level = 9


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: {0} [compress|decompress] [compression-level] [input-file]'.format(sys.argv[0]))
        sys.exit(1)

    if sys.argv[1] == 'compress':
        if len(sys.argv) >= 3:
            compress_file_level = int(sys.argv[2])
        if len(sys.argv) >= 4:
            compress_to_file(sys.argv[3], sys.argv[3] +
