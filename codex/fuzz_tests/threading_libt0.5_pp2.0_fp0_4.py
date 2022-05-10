import threading
threading.stack_size(67108864)

# ##############################################################################
# ############################## INITIALIZATION ################################
# ##############################################################################

# Get the arguments
parser = argparse.ArgumentParser()
parser.add_argument('-i', '--input', required=True, help='Input file')
parser.add_argument('-o', '--output', required=True, help='Output file')
parser.add_argument('-w', '--window', required=True, type=int, help='Window size')
parser.add_argument('-s', '--step', required=True, type=int, help='Step size')
parser.add_argument('-b', '--bins', required=True, type=int, help='Number of bins')
parser.add_argument('-v', '--verbose', required=False, type=int, default=0, help='Verbosity level')
args = parser.parse_args()

# Set the verbosity level
if args.verbose == 1:
    logging.basicConfig
