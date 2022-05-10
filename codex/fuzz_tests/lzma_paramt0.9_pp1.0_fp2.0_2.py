from lzma import LZMADecompressor
LZMADecompressor(max_length=None)

DIR = ''
PATH = os.getcwd()
PARENT_PATH = os.path.join(PATH, os.pardir)

sys.path.insert(0, PARENT_PATH)

from Common.dictionaries import RISK_LABELS


def parse_arguments():
    parser = argparse.ArgumentParser()

    parser.add_argument('--dir',
                        type=str,
                        default=DIR,
                        help='directory in which to store training data')

    parser.add_argument('--user',
                        type=str,
                        help='user in train dataset to retrieve training data')

    parser.add_argument('--window',
                        type=int,
                        help='window of time that the model should use to predict the outcome')

    return parser.parse_args()


def create_new_micro(row):
    return {
        'date': row[1] if (row[1] != None and row[1] != 'None') else row[0],
        **row[2]
    }


def save
