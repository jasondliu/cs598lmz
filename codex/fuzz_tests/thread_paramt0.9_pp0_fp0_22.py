import sys, threading
threading.Thread(target=lambda: sys.stdout.write('')).start() 
import process
import file_utils
import load_model
import utils
import json
import argparse

## for debug
import traceback

_WORKER = 8

## for run process to predict
# predict -p pdf_path -l model_log_path -c model_config_path -o output_path
def predict_process():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p','--pdf_path')
    parser.add_argument('-l','--model_log_path')
    parser.add_argument('-c','--model_config_path')
    parser.add_argument('-o','--output_path')

    args = parser.parse_args()
    print(args)
    # pdf_path = args.pdf_path
    # model_log_path = args.model_log_path
    # model_config_path = args.model_config_path
    # output_path = args.output_path

    pdf_path = './files/data
