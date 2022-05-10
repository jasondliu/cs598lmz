import codecs
codecs.register_error('strict', codecs.ignore_errors)

def main():
    # get the command line arguments
    args = parse_args()

    # set up logging
    logging.basicConfig(level=logging.DEBUG if args.verbose else logging.INFO,
                        format='%(asctime)s %(levelname)s %(message)s')

    # get the list of files to process
    files = get_files(args.input_dir)

    # process the files
    for f in files:
        process_file(f, args.output_dir)

def parse_args():
    parser = argparse.ArgumentParser(description='Convert a directory of XML files to JSON')
    parser.add_argument('input_dir', help='The directory containing the XML files')
    parser.add_argument('output_dir', help='The directory to write the JSON files to')
    parser.add_argument('-v', '--verbose', action='store_true', help='Enable verbose logging')
    return parser.parse_args()

def get_files(input_
