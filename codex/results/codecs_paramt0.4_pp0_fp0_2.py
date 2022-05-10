import codecs
codecs.register_error('replace_with_space', codecs.replace_with_space)

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dataset", help="Path to the dataset")
    parser.add_argument("--batch_size", help="Batch size", type=int, default=32)
    parser.add_argument("--num_epochs", help="Number of epochs", type=int, default=100)
    parser.add_argument("--learning_rate", help="Learning rate", type=float, default=1e-4)
    parser.add_argument("--num_layers", help="Number of layers", type=int, default=1)
    parser.add_argument("--hidden_size", help="Hidden size", type=int, default=512)
    parser.add_argument("--dropout", help="Dropout", type=float, default=0.5)
    parser.add_argument("--gpu", help="GPU device", type=int, default=0)
    parser.add_argument("--save_
