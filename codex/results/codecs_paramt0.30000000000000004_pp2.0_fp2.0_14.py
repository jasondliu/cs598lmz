import codecs
codecs.register_error('strict', codecs.ignore_errors)

def main():
    """
    Main function
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', help='Input file', required=True)
    parser.add_argument('-o', '--output', help='Output file', required=True)
    parser.add_argument('-d', '--delimiter', help='Delimiter', default='\t')
    parser.add_argument('-c', '--column', help='Column to use', default=0)
    parser.add_argument('-s', '--separator', help='Separator', default=' ')
    parser.add_argument('-l', '--lowercase', help='Lowercase', action='store_true')
    parser.add_argument('-u', '--uppercase', help='Uppercase', action='store_true')
    parser.add_argument('-t', '--titlecase', help='Titlecase', action='store_true')
    args = parser.parse_args
