import codecs
codecs.register_error('redact', lambda e: (u'|' * len(e.object), e.end))

def main():
    parser = argparse.ArgumentParser(description="Redact text")
    parser.add_argument('-r', '--recursive', action='store_true',
                        help="Traverse subdirectories recursively")
    parser.add_argument('files', nargs='*',
                        help="Files to redact")
    args = parser.parse_args()

    files = args.files
    if not files:
        files = glob.glob('*.txt')
    if args.recursive:
        files += glob.glob('**/*.txt')
    for f in files:
        print f
        try:
            with codecs.open(f, 'r', 'utf-8', errors='redact') as infile:
                with codecs.open(f.replace('.txt', '.redacted.txt'), 'w', 'utf-8') as outfile:
                    for line in infile:
                        outfile.write(line)
        except
