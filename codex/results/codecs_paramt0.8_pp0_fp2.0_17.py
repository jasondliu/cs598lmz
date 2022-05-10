import codecs
codecs.register_error('ignore', codecs.lookup('ignore'))

logger = logging.getLogger(__name__)


def get_row_reader(row):
    def reader():
        return row

    return reader


class DataFrameManager(object):

    def __init__(self, data_frame):
        self.data_frame = data_frame

    def load(self, source_path, source_format, source_options):
        if source_format == 'csv':
            self.data_frame = self._load_from_csv(source_path, source_options)
        elif source_format == 'json':
            self.data_frame = self._load_from_json(source_path, source_options)
        else:
            raise ValueError('Format %s is not supported' % source_format)
        return self

    def _load_from_csv(self, source_path, source_options):
        reader = self._get_csv_reader(source_path, source_options)
        data_frame = pd.DataFrame(reader)
        self._
