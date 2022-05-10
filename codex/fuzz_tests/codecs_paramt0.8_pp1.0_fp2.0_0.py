import codecs
codecs.register_error('strict', codecs.ignore_errors)

#============================= Controller ==================================

class Controller(object):
    def __init__(self):
        self.root = os.getcwd()
        self.config = configparser.ConfigParser()
        self.config_file = os.path.join(self.root, 'config.ini')
        self.config.read(self.config_file)
        self.logger = logging.getLogger(__name__)

        self.data_path = os.path.join(self.root, 'Data')
        self.entity_path = os.path.join(self.data_path, 'entity')
        self.favicon_path = os.path.join(self.data_path, 'favicon')
        self.icon_path = os.path.join(self.data_path, 'icon')

    def get_db_conn(self):
        db_file = os.path.join(self.data_path, 'data.db')
        if os.path.exists(db_file):
