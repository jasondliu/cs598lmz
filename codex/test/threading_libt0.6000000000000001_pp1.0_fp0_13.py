import threading
threading.stack_size(67108864)

import sys
sys.path.append("../")

from utils import load_data, load_data_with_nan
from train_lstm import train_lstm

if __name__ == "__main__":

    train_df, test_df = load_data_with_nan()
    train_lstm(train_df, test_df)
