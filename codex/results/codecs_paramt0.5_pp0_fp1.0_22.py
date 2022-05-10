import codecs
codecs.register_error('strict', codecs.ignore_errors)

class Config:
    def __init__(self):
        self.config = {}
        self.config_file = 'config.ini'
        self.load()

    def load(self):
        if not os.path.exists(self.config_file):
            self.create()
        else:
            self.config = ConfigParser.RawConfigParser()
            self.config.read(self.config_file)

    def create(self):
        self.config = ConfigParser.RawConfigParser()
        self.config.add_section('config')
        self.config.set('config', 'download_path', 'downloads')
        self.config.set('config', 'max_download_tasks', '10')
        self.config.set('config', 'max_seed_tasks', '10')
        self.config.set('config', 'max_upload_rate', '0')
        self.config.set('config', 'max_download_rate', '0')
        self.config.set('config', '
