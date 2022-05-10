import codecs
codecs.register_error('strict', codecs.ignore_errors)

def main():
    parser = argparse.ArgumentParser(description='Convert a text file to a binary file')
    parser.add_argument('--input', '-i', required=True, help='input text file')
    parser.add_argument('--output', '-o', required=True, help='output binary file')
    parser.add_argument('--encoding', '-e', default='utf-8', help='input text encoding')
    parser.add_argument('--delimiter', '-d', default='\t', help='delimiter between fields')
    parser.add_argument('--fields', '-f', default=None, help='fields to include in output')
    parser.add_argument('--skip', '-s', default=0, type=int, help='number of lines to skip')
    parser.add_argument('--limit', '-l', default=None, type=int, help='number of lines to process')
    parser.add_argument('--verbose', '-v', action='store_
