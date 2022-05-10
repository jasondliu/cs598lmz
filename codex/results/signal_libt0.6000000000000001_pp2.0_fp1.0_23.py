import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

# Parse command line arguments
parser = argparse.ArgumentParser(description='Create a GAN model to generate images of handwritten digits.')
parser.add_argument('--dataset_dir', default='./datasets/mnist', help='Directory of the MNIST dataset')
parser.add_argument('--epochs', default=200, type=int, help='Number of training epochs')
parser.add_argument('--batch_size', default=64, type=int, help='Batch size')
parser.add_argument('--latent_dim', default=100, type=int, help='Dimensionality of the latent space')
parser.add_argument('--n_filters_generator', default=64, type=int, help='Number of filters for the generator network')
parser.add_argument('--n_filters_discriminator', default=64, type=int, help='Number of filters for the discriminator network')
args = parser.parse_args()


# Create the
