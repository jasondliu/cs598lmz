import codecs
codecs.register_error('surrogate_escape', codecs.backslashescape)
import sys

def read_csv(path):
    '''
    :param path: file path
    :return: a list of lists containing rows
    '''
    with codecs.open(path, 'r', encoding='utf8', errors="surrogate_escape") as file:
        # print(path)
        reader = csv.reader(file, quoting=csv.QUOTE_NONNUMERIC)
        return list(reader)

def read_file(path):
    '''
    :param path: file path
    :return: a list of lines
    '''
    with codecs.open(path, 'r', encoding='utf8', errors="surrogate_escape") as file:
        return file.readlines()

def write_csv(path, data):
    '''
    :param path: file path
    :param data: a list of lists containing rows
    :return:
    '''
    with open(path, 'w', newline='') as file:
       
