import types
types.ClassType = type
types.ModuleType = type

try:
    from types import InstanceType
except ImportError:
    pass


def convert_hdf5(filename):
    """
    Convert an HDF5 file to a dictionary.

    :param filename: The filename of the HDF5 file.
    """
    with h5py.File(filename, 'r') as f:
        return convert_hdf5_group(f)


def convert_hdf5_group(group):
    """
    Converts an HDF5 group recursively to a dictionary.

    :param group: The HDF5 group.
    """
    ret = {}
    for name, value in group.items():
        if isinstance(value, h5py.Group):
            ret[name] = convert_hdf5_group(value)
        else:
            if isinstance(value, np.ndarray):
                ret[name] = np.array(value)
            else:
                ret[name] = value.value
    return ret


