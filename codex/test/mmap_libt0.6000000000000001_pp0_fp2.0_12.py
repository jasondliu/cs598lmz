import mmap
import csv

def read_data(filename, delimiter='\t'):
    """ Reads a csv file and returns a list of lists.
    Each sublist contains a row of data from the csv file.
    """
    data = []
    with open(filename, 'rb') as csvfile:
        reader = csv.reader(csvfile, delimiter=delimiter, quoting=csv.QUOTE_NONE)
        for row in reader:
            data.append(row)
    return data

def read_metadata(filename):
    """ Reads the metadata from a csv file and returns a dictionary.
    The keys are the column names and the values are the column descriptions.
    """
    metadata = {}
    with open(filename, 'rb') as csvfile:
        reader = csv.reader(csvfile, delimiter='\t', quoting=csv.QUOTE_NONE)
        for row in reader:
            metadata[row[0]] = row[1]
    return metadata

