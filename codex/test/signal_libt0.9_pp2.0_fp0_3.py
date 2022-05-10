import signal
signal.signal(signal.SIGPIPE, signal.SIG_DFL)

# Parse the command line arguments.
parser = argparse.ArgumentParser()
parser.add_argument('--mag', help='Magnification.', action='store_true')
args = parser.parse_args()
if args.mag:
    mag = True
else:
    mag = False


# Shortcut functions to manipulate list of transforms.
def transform_below(transform_list, container_transform):
    transform_list[0:0] = [ container_transform ]

def transform_above(transform_list, container_transform):
    transform_list.append(container_transform)

# Check the given file name (full path) meet the requirements.
def check_file(filename):
    is_ok = False
