import mmap
import argparse

#TODO: make a class for this

def get_args():
    parser = argparse.ArgumentParser(description='Convert csv file to bin')
    parser.add_argument('-i','--input', help='Input file',required=True)
    parser.add_argument('-o','--output',help='Output file', required=True)
    parser.add_argument('-t','--type',help='Type of data (float, int, long, short)', required=True)
    parser.add_argument('-c','--channels',help='Number of channels', required=True)
    args = parser.parse_args()
    return args

def main():
    args = get_args()
    dataType = {'float':'f', 'int':'i', 'long':'q', 'short':'h'}
