import codecs
codecs.register_error('strict', codecs.ignore_errors)

def get_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--train_file', type=str, default='data/train.txt')
    parser.add_argument('--dev_file', type=str, default='data/dev.txt')
    parser.add_argument('--test_file', type=str, default='data/test.txt')
    parser.add_argument('--batch_size', type=int, default=32)
    parser.add_argument('--epochs', type=int, default=10)
    parser.add_argument('--embedding_size', type=int, default=300)
    parser.add_argument('--hidden_size', type=int, default=200)
    parser.add_argument('--dropout', type=float, default=0.5)
    parser.add_argument('--learning_rate', type=float, default=0.001)
    parser.add_argument('--decay_step', type=int, default=10000)
