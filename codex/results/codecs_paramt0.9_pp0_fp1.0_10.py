import codecs
codecs.register_error('surrogate_pass', codecs.surrogateescape)

try:
    import hgvs.parser
except ImportError:
    print('`hgvs` module needs to be installed: pip install hgvs')
    sys.exit(1)

__version__ = '1.0.8'

parser = argparse.ArgumentParser(description=__doc__,
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('--version', action='version', version='%(prog)s '+__version__)
parser.add_argument('-i', '--input', required=True,
        help='VCF input file')
parser.add_argument('-o', '--output', required=True,
        help='output file name')
parser.add_argument('-m', '--mode', default='gen', choices=['gen','fasta','f','fasta'],
        help="if set to 'gen', dbNSFP_gene is used.\n"
        "if set to 'fasta' (default
