from bz2 import BZ2Decompressor
BZ2Decompressor

import xml.etree.cElementTree as ET

def open_pkl(path):
    with open(path, 'rb') as f:
        return pickle.load(f)

def save_pkl(data, path):
    with open(path, 'wb') as f:
        pickle.dump(data, f)
        
def process_map(filename):
    """
    Iteratively process each XML element in the map file, adding each of
    the elements to a list, and return that list.
    Args:
        filename: the name of the map file
    Returns:
        list of element, in the order of the XML file
    """
    # Append all elements to a big list
    biglist = []
    for _, element in ET.iterparse(filename):
        biglist.append(element)
    return biglist

def create_name_id_dct(dct):
    """
    Takes a dictionary of users, their id and their name and returns a dictionary of ids and names
    Args:
        dct: 

