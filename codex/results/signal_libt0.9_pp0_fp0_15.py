import signal
signal.signal(signal.SIGPIPE, signal.SIG_DFL)

###########################################################################
class FilterLoci(JOB, LMF):
    """
    Wrapper for qsub'ing the filterloci script
    """
    def __init__(self, cmd_options=None, arg_options=None, stdout=None):
        # initialize parent class
        super(FilterLoci, self).__init__(cmd_options)

        self.prog = os.path.basename(sys.argv[0])
        self.cmd_options = cmd_options
        self.arg_options = arg_options

        self.results = None
        self.stdout = stdout
        self.filter_type = None
        self.min_id = None
        self.min_snps = None
        self.min_indels = None
        self.out_type = None
        self.sample_ids = None
        self.samples_to_use = []
        self.filter_type = None
        self.min_id = None

