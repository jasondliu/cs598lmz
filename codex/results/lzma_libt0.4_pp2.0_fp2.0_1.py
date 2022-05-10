import lzma
lzma.LZMA_ERROR_FORMAT = 1

def main():
    parser = argparse.ArgumentParser(description='Convert a .xz file to a .tar.gz file')
    parser.add_argument('xz_file', type=str,
                        help='The .xz file to convert')
    parser.add_argument('tar_file', type=str,
                        help='The .tar.gz file to write')
    args = parser.parse_args()

    # Read the xz file
    with lzma.open(args.xz_file, 'rb') as f:
        xz_data = f.read()

    # Write the tar.gz file
    with gzip.open(args.tar_file, 'wb') as f:
        f.write(xz_data)

if __name__ == '__main__':
    main()
