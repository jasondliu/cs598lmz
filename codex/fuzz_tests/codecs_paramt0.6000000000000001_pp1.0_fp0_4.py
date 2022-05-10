import codecs
codecs.register_error('strict', codecs.ignore_errors)

def parser_args():
    parser = argparse.ArgumentParser(
        description='Convert the output of the Star-CCM+ post-process to a '
        'suitable format for the OpenFoam post-process.',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-i', '--input', metavar='FILE',
                        help='input file', required=True)
    parser.add_argument('-o', '--output', metavar='FILE',
                        help='output file', required=True)
    parser.add_argument('-s', '--separator', metavar='STRING', default=' ',
                        help='separator for the output file')
    return parser.parse_args()

def main():
    args = parser_args()

    #Read the input file
    with open(args.input, 'r') as f:
        lines = f.readlines()

    #Define the list of variables that will be kept in the output

