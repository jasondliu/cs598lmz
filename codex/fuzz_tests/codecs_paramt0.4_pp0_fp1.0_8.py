import codecs
codecs.register_error('ignore', codecs.lookup('utf-8'))

#------------------------------------------------------------------------------
#
#------------------------------------------------------------------------------

def parse_args():
    parser = argparse.ArgumentParser(description='Parse the GEDCOM file')
    parser.add_argument('--gedcom_file', help='Path to the GEDCOM file', required=True)
    parser.add_argument('--gedcom_encoding', help='GEDCOM file encoding', default='latin-1')
    parser.add_argument('--gedcom_date_format', help='GEDCOM date format', default='%d %b %Y')
    parser.add_argument('--output_file', help='Path to the output file', required=True)
    parser.add_argument('--output_encoding', help='Output file encoding', default='utf-8')
    parser.add_argument('--output_format', help='Output file format', default='csv')
    parser.add_argument('--output_delimiter', help='Output file delimiter', default=';')
    parser.add_argument('--output_quote
