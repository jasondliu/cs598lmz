import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'cp65001' else None)

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--data_dir', default='data/squad', help='data directory')
    parser.add_argument('--dataset', default='squad', help='dataset')
    parser.add_argument('--embed_dir', default='embedding', help='embedding directory')
    parser.add_argument('--embedding', default='glove', help='embedding')
    parser.add_argument('--embedding_dim', type=int, default=300, help='embedding dimension')
    parser.add_argument('--hidden_size', type=int, default=100, help='hidden size')
    parser.add_argument('--num_layers', type=int, default=1, help='number of layers')
    parser.add_argument('--dropout', type=float, default=0.2, help='dropout')
    parser.add_argument
