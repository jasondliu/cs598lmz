import socket

from my_lstm import create_data, train_model, predict_model
from my_dataset import load_dataset, make_dataset
from my_preprocess import read_data, pre_process
from my_preprocess import read_data_from_file, pre_process_from_file

parser = argparse.ArgumentParser(description='LSTM')
parser.add_argument('--model_path', type=str, default='../model/lstm/lstm.h5')
parser.add_argument('--model_history_path', type=str, default='../model/lstm/lstm_history.json')
parser.add_argument('--model_dict_path', type=str, default='../model/lstm/lstm_dict.txt')
parser.add_argument('--datasets_path', type=str, default='../datasets/lstm')
parser.add_argument('--dataset_train_path', type=str, 
                    default='../datasets/lst
