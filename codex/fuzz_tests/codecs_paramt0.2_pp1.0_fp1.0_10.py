import codecs
codecs.register_error('strict', codecs.ignore_errors)

def main():
    parser = argparse.ArgumentParser(description='Convert a file to a list of tokens')
    parser.add_argument('-i', '--input', help='Input file', required=True)
    parser.add_argument('-o', '--output', help='Output file', required=True)
    parser.add_argument('-l', '--language', help='Language', required=True)
    parser.add_argument('-t', '--tokenizer', help='Tokenizer', required=True)
    parser.add_argument('-s', '--sentence-tokenizer', help='Sentence tokenizer', required=True)
    parser.add_argument('-d', '--debug', help='Debug', action='store_true')
    args = parser.parse_args()

    if args.debug:
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.INFO)

    if args.language == 'en':
        tokenizer = EnglishToken
