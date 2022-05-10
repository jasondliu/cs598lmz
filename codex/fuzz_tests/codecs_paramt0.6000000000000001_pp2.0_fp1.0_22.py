import codecs
codecs.register_error('replace_with_space', lambda e: (u' ', e.start + 1))

# python 2/3 compatibility
from __future__ import print_function

# global variables
args = None

# ------------------------------------------------------------------------------
# 
# ------------------------------------------------------------------------------


def main():

    # parse arguments
    global args
    args = parse_args()

    # read the data
    data = read_data(args.input_file, args.encoding)

    # extract the relevant data
    if args.column is not None and args.column >= 0:
        data = extract_column(data, args.column)

    # transform the data
    if args.trim:
        data = trim_data(data)

    if args.lower:
        data = lower_data(data)

    # sort the data
    if args.sorted:
        data = sorted(data)

    # write the data
    write_data(data, args.output_file, args.encoding)


# ------------------------------------------------------------------------------
# 
# ------------------------------------------------------------------------------


def parse_args():

    parser = argparse.
