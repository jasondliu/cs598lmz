import mmap
from IPython import display


class Mapping:
    """
    Mapping: Class for reading the binary file container data and converting it to a numpy array.
    """

    def __init__(self, filename: str, filename_2d: str):
        """
        :param filename: File path of the binary container
        :param filename_2d: File path of the 2D map
        """
        self.__data_file = filename
        self.__data_file_2d = filename_2d

    def read_2d_data(self):
        """
        Reads the 2D map data into a numpy array. Used for calculating 2D histogram and comparison with 3D mapping.
        :return: 2D map data
        """
        data = np.fromfile(self.__data_file_2d, dtype=np.uint64)
        return data

    def read_3d_data(self):
        """
        Reads the 3D mapping data into a numpy array.
        :return: 3D mapping data
        """
        with open(self
