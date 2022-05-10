import codecs
codecs.register_error('ignore', codecs.ignore_errors)

class Backend(object):
    def __init__(self, config):
        self.config = config
        self.__initialize()

    def __initialize(self):
        """
        Initialize the backend.
        """
        self.tags = []
        self.notes = []

        # Set up the config directory.
        self.config_dir = self.config['config_dir']
        if not os.path.exists(self.config_dir):
            os.makedirs(self.config_dir)

        # Set up the notes directory.
        self.notes_dir = self.config['notes_dir']
        if not os.path.exists(self.notes_dir):
            os.makedirs(self.notes_dir)

        # Set up the notes file.
        self.notes_file = os.path.join(self.config_dir, 'notes')
        if not os.path.exists(self.notes_file):
            open(self.notes_file, 'w').close()
