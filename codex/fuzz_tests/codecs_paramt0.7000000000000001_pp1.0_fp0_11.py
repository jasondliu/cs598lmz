import codecs
codecs.register_error('strict', codecs.ignore_errors)

logger = logging.getLogger(__name__)


def open_csv(csv_file_name, encoding='utf-8'):
    """
    Open CSV file and handle encoding.

    :param csv_file_name: Name of file to open.
    :param encoding: Encoding to decode file with.
    :return: Opened file handle.
    """
    return codecs.open(csv_file_name, mode='r', encoding=encoding, errors='strict')


def read_csv(f):
    """
    Read CSV file into data structure.

    :param f: File handle to read from.
    :return: List of dictionaries with keys from the header row and values from the rows.
    """
    reader = csv.DictReader(f)
    return [row for row in reader]


def write_csv(f, rows, headers=None, delimiter='\t', encoding='utf-8'):
    """
    Write rows to file as CSV.

    :param f: File
