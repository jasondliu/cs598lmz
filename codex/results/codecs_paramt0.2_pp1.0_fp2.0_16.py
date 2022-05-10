import codecs
codecs.register_error('strict', codecs.ignore_errors)

def main():
    parser = argparse.ArgumentParser(description='Generate a list of all the words in a corpus')
    parser.add_argument('--corpus', required=True, help='Path to the corpus')
    parser.add_argument('--output', required=True, help='Path to the output file')
    args = parser.parse_args()

    words = set()
    with codecs.open(args.corpus, 'r', 'utf-8', 'strict') as f:
        for line in f:
            for word in line.split():
                words.add(word)

    with codecs.open(args.output, 'w', 'utf-8') as f:
        for word in sorted(words):
            f.write(word + '\n')

if __name__ == '__main__':
    main()
