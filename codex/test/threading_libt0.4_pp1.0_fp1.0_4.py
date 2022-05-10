import threading
threading.stack_size(67108864)

def main():
    # Parse command line arguments
    parser = argparse.ArgumentParser(
        description='Run Forest on the model')
    parser.add_argument(
        '--model',
        type=str,
        default='',
        help='Path to the model')
    parser.add_argument(
        '--data',
        type=str,
        default='',
        help='Input data')
    parser.add_argument(
        '--output',
        type=str,
        default='',
        help='Path to output file')
    parser.add_argument(
        '--epochs',
        type=int,
        default=1,
        help='Number of epochs to run')
    parser.add_argument(
        '--batch_size',
        type=int,
        default=1,
        help='Batch size')
    parser.add_argument(
        '--num_classes',
        type=int,
        default=1000,
        help='Number of classes')
