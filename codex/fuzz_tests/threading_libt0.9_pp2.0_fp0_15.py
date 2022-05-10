import threading
threading.stack_size(67108864)

# Initialize the parser with the default parameters.
default_args = dict(
    iteration=0,
    learning_rate_genre=0.001,
    learning_rate_network=0.001,
    regularization=1e-4,
    batch_size=32,
    max_iterations=1000,
    keep_probability=1.0,
    weight_decay=0.001,
    random_seed=int(time.time()),
    num_genre_per_sample=1)

parser = argparse.ArgumentParser(description='Run DUMBO.')
parser.add_argument('--dataset_dir', dest='dataset_dir', required=True,
                    help='Dataset directory containing dataset.pickle')
parser.add_argument('--dumbo_dir', dest='dumbo_dir', required=True,
                    help='DUMBO directory containing src/')
parser.add_argument('--dumbo_data_dir', dest='dumbo_data_dir', required=
