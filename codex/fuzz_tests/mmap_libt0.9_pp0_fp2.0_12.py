import mmap
import re
import pandas as pd


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='python script to move a set of files from a gzipped striped file back to individual files.  This is useful in order to index the file using tools such as BWA.\n')
    parser.add_argument('-r','--read-buffer-size', help='size of the read buffer in bytes (multiply by 3 to estimate memory footprint in bytes)', type=int, default = 10**6)
    parser.add_argument('-z','--zcat-buffer-size', help='size of zcat buffer in lines', type=int, default=40)
    parser.add_argument('-f','--file-list', help='list of files to extract', type=argparse.FileType('r'), required=True)
    parser.add_argument('-d','--dest-directory', help='directory to extract files to', type=str, required=True)
    parser.add_argument('-t','--temp-directory', help='directory to extract files
