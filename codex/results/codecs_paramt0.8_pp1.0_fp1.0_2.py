import codecs
codecs.register_error('Ignore', lambda exc: (u'', exc.end))

def encode_opt(options, opt_str, value, parser):
    setattr(parser.values, opt_str.replace('-', '_'), value.encode('ascii', 'ignore'))

parser = optparse.OptionParser()
parser.add_option('--iris', dest='iris_path', action='store',
                  help='Path to iris-*.c file')
parser.add_option('--iras', dest='iras_path', action='store',
                  help='Path to iras-*.c file')
parser.add_option('--input', dest='input_path', action='store',
                  help='Path to input file')
parser.add_option('--output', dest='output_path', action='store',
                  help='Path to output file')
parser.add_option('--gen', dest='gen_path', action='store',
                  help='Path to gen.py')
parser.add_option('--debug', dest='debug', action='store_true',
                  help='Print
