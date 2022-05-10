import codecs
codecs.register_error('strict', codecs.ignore_errors)

def main(infile, outfile, remove_unmappable=True):
    """
    Remove unmappable characters from a string.
    """
    with codecs.open(infile, 'r', 'utf-8') as fi:
        with codecs.open(outfile, 'w', 'utf-8') as fo:
            for line in fi:
                line = line.strip()
                if line:
                    if remove_unmappable:
                        line = line.encode('ascii', 'strict').decode('ascii')
                    fo.write('%s\n' % line)

if __name__ == '__main__':
    infile = sys.argv[1]
    outfile = sys.argv[2]
    main(infile, outfile)
