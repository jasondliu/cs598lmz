import bz2
bz2.BZ2Compressor

class Dataset(object):

    def __init__(self, name='mnist', dataset_path=None):
        self.name = name
        self.dataset_path = dataset_path
        self.img_size = 28
        self.num_channels = 1
        if name == 'mnist':
            self.num_classes = 10
        elif name == 'fashion_mnist':
            self.num_classes = 10

        if dataset_path is not None:
            self.dataset_path = dataset_path
        else:
            self.dataset_path = './{}/'.format(self.name)

    def get_batch(self, batch_size, split_name='train'):
        split_path = os.path.join(self.dataset_path, split_name)

        assert os.path.exists(split_path), 'Split {} not found'.format(split_name)

        img_paths = []
        img_paths = glob.glob(split_path
