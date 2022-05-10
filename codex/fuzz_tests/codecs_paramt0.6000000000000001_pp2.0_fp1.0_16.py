import codecs
codecs.register_error('surrogate_escape', codecs.replace_errors)

def main(args):
    if len(args) != 3:
        print('Usage:', args[0], '<infile> <outfile>', file=sys.stderr)
        sys.exit(1)

    infile = args[1]
    outfile = args[2]

    with codecs.open(infile, 'r', 'UTF-8', 'surrogate_escape') as f:
        lines = f.readlines()
    with codecs.open(outfile, 'w', 'UTF-8') as f:
        for line in lines:
            line = line.strip()
            if line:
                f.write(line + '\n')

if __name__ == '__main__':
    main(sys.argv)
