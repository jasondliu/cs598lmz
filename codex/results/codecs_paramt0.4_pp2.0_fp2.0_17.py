import codecs
codecs.register_error('strict', codecs.ignore_errors)

def main():
    parser = argparse.ArgumentParser(description='Convert a .csv file to a .tsv file.')
    parser.add_argument('infile', help='input .csv file')
    parser.add_argument('outfile', help='output .tsv file')
    args = parser.parse_args()

    with codecs.open(args.infile, 'r', 'utf-8') as infile:
        with codecs.open(args.outfile, 'w', 'utf-8') as outfile:
            for line in infile:
                outfile.write(line.replace(',', '\t'))

if __name__ == '__main__':
    main()
