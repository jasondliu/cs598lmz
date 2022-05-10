import threading
threading.stack_size(50000000)  #40MB stack
sys.setrecursionlimit(2**20)
default_timer = time.time

logger = logging.getLogger(__name__)


class ProcessLine(object):
    """Takes input from the generator and produces output"""

    def __init__(self, params, dump_dir, clump_dir, chrm, block_size,
                 logger=None, tot_blocks=1, color_updates=False,
                 total_elements=0, chrm_pos=None, ref_gt_fname=None):

        self.block_size = block_size
        self.chrm_pos = chrm_pos if chrm_pos is not None else params.chrm_pos

        self.in_gen = None
        self.dump_dir = dump_dir
        self.clump_dir = clump_dir
        self.chrm = chrm
        self.params = params
        self.tot_blocks = tot_blocks

        self.color_updates = color_updates
       
