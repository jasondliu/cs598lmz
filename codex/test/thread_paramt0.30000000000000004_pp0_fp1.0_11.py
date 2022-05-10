import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n')).start()

def get_arguments():
    parser = argparse.ArgumentParser(description='Script to run a trained model on a dataset.')
    parser.add_argument('--model', type=str, help='Path to the model file.')
    parser.add_argument('--dataset', type=str, help='Path to the dataset.')
    parser.add_argument('--batch_size', type=int, default=64, help='Batch size.')
    parser.add_argument('--num_workers', type=int, default=4, help='Number of workers.')
    parser.add_argument('--shuffle', action='store_true', help='Whether to shuffle the data.')
    parser.add_argument('--num_classes', type=int, default=2, help='Number of classes.')
    parser.add_argument('--num_channels', type=int, default=3, help='Number of channels.')
