import codecs
codecs.register_error('replace_with_space', codecs.lookup_error('ignore'))

def generate_data(filename, n_samples):
    """
    Generate fake data with a given number of samples.
    :param filename: str
    :param n_samples: int
    :return: None
    """
    with open(filename, 'w') as f:
        for i in range(n_samples):
            f.write('{}\n'.format(i))


def load_data(filename):
    """
    Load data from a file and split the lines into a list.
    :param filename: str
    :return: list
    """
    with open(filename) as f:
        data = f.read().splitlines()
    return data


def write_data(filename, data):
    """
    Write data to a file.
    :param filename: str
    :param data: list
    :return: None
    """
    with open(filename, 'w') as f:
        f.write('\n'.join(data))


def load
