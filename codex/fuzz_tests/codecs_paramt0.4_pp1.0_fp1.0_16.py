import codecs
codecs.register_error('strict', codecs.ignore_errors)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', '-i', required=True, type=str, help='input file')
    parser.add_argument('--output', '-o', required=True, type=str, help='output file')
    parser.add_argument('--max_length', '-m', default=100, type=int, help='max length of input sequence')
    parser.add_argument('--min_frequency', '-f', default=0, type=int, help='min frequency of words')
    parser.add_argument('--seed', '-s', default=0, type=int, help='random seed')
    parser.add_argument('--debug', action='store_true', help='debug mode')
    args = parser.parse_args()

    if args.debug:
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.INFO)

    logging.info('reading corpus ...
