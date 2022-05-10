import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

from config import *
from utils import *
from data_utils import *

def get_params():
    parser = argparse.ArgumentParser(description='Short sample app')
    parser.add_argument('-input', action="store", dest="input")
    parser.add_argument('-output', action="store", dest="output")
    return parser.parse_args()

def main(input_file, output_csv):
    # input_file = "./data/test_data.json"
    input_data = pd.read_json(input_file)

    # TODO: Clean data
    # 沒有計算機相關課程的資料不好處理，直接捨棄不用
    input_data = input_data.dropna()

    # Preprocess data
    input_data = preprocess_
