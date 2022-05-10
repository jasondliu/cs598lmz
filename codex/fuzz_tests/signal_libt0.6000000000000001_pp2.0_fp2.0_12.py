import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

# Custom modules
import pyhf
from pyhf.contrib.gof import ks_test

# Local modules
import utils as u
import plotting as pl
import model as m

# Use LaTeX
pl.rc('text', usetex=True)
pl.rc('font', family='serif')

# Parse command line arguments
parser = argparse.ArgumentParser(description='Run a fit')
parser.add_argument('-v', '--verbose', type=int,
                    help='verbosity level [0-3] (default: 1)', default=1)
parser.add_argument('-s', '--seed', type=int,
                    help='random number generator seed', default=1234)
args = parser.parse_args()

# Set verbosity level
vb = u.Verbosity(args.verbose)

# Set random number generator seed
np.random.seed(args.seed)

# Set pyhf verbosity level

