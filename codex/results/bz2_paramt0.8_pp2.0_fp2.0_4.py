from bz2 import BZ2Decompressor
BZ2Decompressor.decompress=bz2_decompress_patch

def main():
    parser = argparse.ArgumentParser(description='Generate a bootfile.csv from a .wim')
    parser.add_argument('-o', '--outfile',  type=argparse.FileType('w'), help='output bootfile.csv', required=True)
    parser.add_argument('-w', '--wim-file', type=argparse.FileType('rb'), help='input .wim', required=True)
    args = parser.parse_args()
    mwim = MWIM(args.wim_file)
    for b in mwim.list_bootable_images():
        print(b.index, b.arch, file=args.outfile)

if __name__ == '__main__':
    main()
