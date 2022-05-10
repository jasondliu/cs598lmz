import codecs
codecs.register_error('strict', codecs.ignore_errors)


def main():
    parser = argparse.ArgumentParser(
        description='Create .mo files from .po files.')
    parser.add_argument(
        '--version', action='version', version='%(prog)s ' + __version__)
    parser.add_argument('-o', '--output-dir', help='output directory')
    parser.add_argument('--strict', action='store_true',
                        help='Error on warnings (exit code 1).')
    parser.add_argument('po_file', help='PO file to compile')

    args = parser.parse_args()

    po_file = os.path.abspath(args.po_file)
    domain = os.path.splitext(os.path.basename(po_file))[0]

    if args.output_dir:
        output_dir = os.path.abspath(args.output_dir)
    else:
        output_dir = os.path.dirname(po_file)

    mo_file
