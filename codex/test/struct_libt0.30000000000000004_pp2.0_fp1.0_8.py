import _struct
import time
import sys

# -------------------------------------------------
# -------------- START OF PROGRAM -----------------
# -------------------------------------------------

# -------------------------------------------------
# -------------- START OF FUNCTIONS ---------------
# -------------------------------------------------

def get_data(data_type, data_size, data_format, data_file):
    """
    Function to read data from a file
    :param data_type: type of data to be read
    :param data_size: size of data to be read
    :param data_format: format of data to be read
    :param data_file: file to read data from
    :return: data read from file
    """
    data = data_file.read(data_size)
    return _struct.unpack(data_format, data)[0]

