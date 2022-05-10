import signal
signal.signal(signal.SIGPIPE, signal.SIG_DFL)

from pandas.io.parsers import read_csv
import matplotlib.pyplot as plt


def load_dataset(name):
    """Loads the dataset.

    The dataset is downloaded automatically the first time this method is called.
    The downloaded files are stored in a cache folder in the user home folder.

    Parameters
    ----------
    name : str
        Name of the dataset (possible values are 'yesno' or 'digits').

    Returns
    -------
    data : ndarray (n_samples, n_features)
        The input data.
    target : ndarray (n_samples,)
        The target values.
    """
    if name == 'yesno':
        data, target = _load_yesno()
    elif name == 'digits':
        data, target = _load_digits()
    else:
        raise ValueError('Unknown dataset: %s' % name)
    return data, target


