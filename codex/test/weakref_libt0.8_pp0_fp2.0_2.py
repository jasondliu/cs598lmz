import weakref

import numpy as np

def _get_all_keys_in_tree(h5file):
    """Return a list with all keys in the tree of `h5file`

    :param h5file:
        Input HDF5 File
    """

    def __get_all_keys(h5g):
        _keys = []
        for _key in h5g.keys():
            if isinstance(h5g[_key], h5py._hl.dataset.Dataset):
                _keys.append(_key)
            elif isinstance(h5g[_key], h5py.Group):
                _keys.append(_key)
                _keys += [_key + '/' + _nkey for _nkey
                          in __get_all_keys(h5g[_key])]

        return _keys

    return __get_all_keys(h5file)


