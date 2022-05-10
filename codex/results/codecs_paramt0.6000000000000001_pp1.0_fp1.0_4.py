import codecs
codecs.register_error('replace_with_unknown', lambda e: (u'<unk>', e.start + 1))

# Parse input arguments
parser = argparse.ArgumentParser()
parser.add_argument(
    '--data_dir',
    type=str,
    default='/tmp/data',
    help='Directory for storing input data')

parser.add_argument(
    '--train_dir',
    type=str,
    default='/tmp/data',
    help='Directory for storing input data')

parser.add_argument(
    '--num_epochs',
    type=int,
    default=2,
    help='Number of epochs for training')

parser.add_argument(
    '--num_classes',
    type=int,
    default=4,
    help='Number of classes')

parser.add_argument(
    '--num_validation_samples',
    type=int,
    default=800,
    help='Number of validation samples')

parser.add_argument(
    '--num_train_steps
