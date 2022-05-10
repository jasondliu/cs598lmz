import codecs
codecs.register_error('strict', codecs.ignore_errors)

# python 2/3 compatibility
import six

# check for python 2.7 or greater
if sys.version_info[:2] < (2, 7):
    sys.exit('This script requires Python 2.7 or greater.')

# check for pyyaml
try:
    import yaml
except ImportError:
    sys.exit('This script requires PyYAML.')


def main():
    """
    Main function.
    """

    # parse arguments
    args = parse_args()

    # read input file
    with open(args.input_file, 'rb') as f:
        data = yaml.load(f)

    # remove null values
    data = remove_null_values(data)

    # convert to JSON
    json_data = json.dumps(data, sort_keys=True, indent=4, separators=(',', ': '))

    # write output file
    with open(args.output_file, 'wb') as f:
        f.write(six.b(json
