import codecs
codecs.register_error('strict', codecs.ignore_errors)

def main():
    fname = sys.argv[1]
    outname = sys.argv[2]
    outfile = open(outname, 'w')
    with codecs.open(fname, encoding='utf-8', errors='strict') as f:
        for line in f:
            line = line.strip()
            parts = line.split('\t')
            if len(parts) != 2:
                print('skipping line: ' + line, file=sys.stderr)
                continue
            outfile.write(parts[1] + '\n')
    outfile.close()

if __name__ == '__main__':
    main()
