import signal
signal.signal(signal.SIGPIPE, signal.SIG_DFL) # IOError: Broken pipe
from logging import INFO
from logging import basicConfig
from logging import getLogger

logger = getLogger(__name__)
basicConfig(format='%(asctime)s %(levelname)s %(message)s', level=INFO)


def parse_args():
    """
    Command line argument parser for this script
    :return: arguments
    """
    parser = ArgumentParser("Codes for i2v_visualization")
    parser.add_argument("--cpu", action="store_const", const="cpu",
                        default="cpu", help="Use CPU")
    parser.add_argument("--gpu", nargs="?", type=int, default=0,
                        const=0, help="Use GPU, or use GPU n")
    parser.add_argument("--img", required=True, help="Input image path")

    return parser.parse_args()


