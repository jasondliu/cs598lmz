import codecs
codecs.register_error('strict', codecs.ignore_errors)

def parse_args():
    parser = argparse.ArgumentParser(description='Script for training/testing a model')
    parser.add_argument('--model_config', type=str, help='file containing the configuration of the model')
    parser.add_argument('--train', action='store_true', help='Train the model')
    parser.add_argument('--test', action='store_true', help='Test the model')
    parser.add_argument('--test_folder', type=str, help='Folder containing the test data')
    parser.add_argument('--output_folder', type=str, help='Folder where to save the model results')
    parser.add_argument('--model_folder', type=str, help='Folder where to save the model')
    parser.add_argument('--model_name', type=str, help='Name of the model')
    parser.add_argument('--embs_file', type=str, help='File containing the embeddings')
    parser.add_argument('--embs_type', type
