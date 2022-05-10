import threading
threading.stack_size(67108864)



def main():
    # create the parser
    parser = argparse.ArgumentParser(description='CSV file to binary converter')
    # add arguments
    parser.add_argument('-f', '--file', help='path to the CSV file', required=True)
    parser.add_argument('-v', '--verbose', help='verbose mode', action='store_true', default=False)
    # parse the arguments
    args = parser.parse_args()
    # check if valid arguments
    if args.verbose:
        print('CSV file path:', args.file)
    # convert CSV file to binary file
    csv_to_binary(args.file, args.verbose)


def csv_to_binary(csv_file, verbose=False):
    # read CSV file
    if verbose:
        print('Reading CSV file...')
    with open(csv_file, 'r') as f:
        reader = csv.reader(f)
        csv_data = list(reader)
