import codecs
codecs.register_error('strict', codecs.ignore_errors)

#-------------------------------------------------------------------------------

def main():
    """
    Main function.
    """

    # parse command line
    parser = argparse.ArgumentParser(description="""
    This script converts a given text file to a list of words.
    """)
    parser.add_argument('-i', '--input', dest='input', type=str, required=True,
                        help='input text file')
    parser.add_argument('-o', '--output', dest='output', type=str, required=True,
                        help='output text file')
    parser.add_argument('-l', '--lowercase', dest='lowercase', action='store_true',
                        help='lowercase all words')
    parser.add_argument('-s', '--split', dest='split', action='store_true',
                        help='split words at punctuation')
    parser.add_argument('-p', '--punctuation', dest='punctuation', type=str,
                        help='punctuation characters to split words at')
    parser.
