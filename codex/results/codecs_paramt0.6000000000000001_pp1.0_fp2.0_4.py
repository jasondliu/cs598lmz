import codecs
codecs.register_error("surrogateescape", codecs.surrogateescape_error)

#import logging
#logging.basicConfig(level=logging.DEBUG)

def main():
    parser = argparse.ArgumentParser(description='Convert between a number of formats.')
    parser.add_argument('--input', '-i', help='input file')
    parser.add_argument('--input-format', '-I', help='input format', choices=['conllu', 'conll09', 'conll06', 'conll06-disco', 'conllx', 'conllx-disco'])
    parser.add_argument('--output', '-o', help='output file')
    parser.add_argument('--output-format', '-O', help='output format', choices=['conllu', 'conll09', 'conll06', 'conll06-disco', 'conllx', 'conllx-disco'])
    parser.add_argument('--tokenize', '-t', action='store_true', help='tokenize input file')
   
