import mmap

def init_parser():
    parser = argparse.ArgumentParser(description='Add header to a file.')
    parser.add_argument('-i', '--infile', dest='infile', help='input file')
    parser.add_argument('-o', '--outfile', dest='outfile', help='output file')
    parser.add_argument('-t', '--header', dest='header', help='header file')
    parser.add_argument('-s', '--skip', dest='skip', type=int, default=0, help='number of lines to skip in input file')
    return parser

def main():
    parser = init_parser()
    args = parser.parse_args()
    if not args.infile or not args.outfile or not args.header:
        parser.error('Incorrect number of arguments.')

    ifile = open(args.infile, 'r+b')
    s = mmap.mmap(ifile.fileno(), 0)
    ofile = open(args.outfile, 'w')
    hfile
