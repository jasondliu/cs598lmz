import codecs
codecs.register_error('strict', codecs.ignore_errors)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', '-i', required=True, help='Path to input file')
    parser.add_argument('--output', '-o', required=True, help='Path to output file')
    parser.add_argument('--chunk_size', '-c', default=1000, type=int, help='Number of lines to read at once')
    parser.add_argument('--encoding', '-e', default='utf-8', help='File encoding')
    args = parser.parse_args()

    with open(args.input, 'r', encoding=args.encoding) as f:
        with open(args.output, 'w', encoding=args.encoding) as out:
            for i, chunk in enumerate(chunked(f, args.chunk_size)):
                print('Processing chunk {}'.format(i))
                out.write(''.join(chunk))

if __name__ == '__main__
