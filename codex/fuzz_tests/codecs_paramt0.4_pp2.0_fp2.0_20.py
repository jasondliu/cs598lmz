import codecs
codecs.register_error('strict', codecs.ignore_errors)

def main(argv):
    parser = argparse.ArgumentParser(description='Convert a CoNLL-X file to a CoNLL-U file.')
    parser.add_argument('--input', '-i', type=str, help='input file in CoNLL-X format', required=True)
    parser.add_argument('--output', '-o', type=str, help='output file in CoNLL-U format', required=True)
    parser.add_argument('--encoding', '-e', type=str, help='encoding of the input file', default='utf-8')
    parser.add_argument('--language', '-l', type=str, help='language of the input file', required=True)
    parser.add_argument('--tagger', '-t', type=str, help='tagger used to tag the input file', required=True)
    parser.add_argument('--version', '-v', type=str, help='version of the tagger', required=True)
    args
