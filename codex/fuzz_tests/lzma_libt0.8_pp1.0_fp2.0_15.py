import lzma
lzma._encode(_encode)
lzma._decode(_decode)

# --------------------------------------------------------------------
# MAIN

def main():
    p = argparse.ArgumentParser()
    p.add_argument('--in', '-i', dest='input', metavar='FILE',
            required=True, help='input file')
    p.add_argument('--out', '-o', dest='output', metavar='FILE',
            required=True, help='output file')
    args = p.parse_args()

    stdin = False
    if args.input == '-':
        stdin = True

    stdout = False
    if args.output == '-':
        stdout = True

    if stdin:
        infile = sys.stdin.buffer
    else:
        infile = open(args.input, 'rb')

    if stdout:
        outfile = sys.stdout.buffer
    else:
        outfile = open(args.output, 'wb')

    try:
        with infile, outfile:
           
