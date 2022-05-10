import codecs
codecs.register_error('surrogate_or_strict', codecs.surrogateescape)

def get_args():
    """
    Parse command line arguments
    """
    parser = argparse.ArgumentParser(description="Saves the list of file hashes for a directory tree.")
    parser.add_argument('root', help="Root directory to hash")
    parser.add_argument('-o', '--output', help="Output file to save hashes to")
    parser.add_argument('-a', '--algorithm', help="Hashing algorithm to use, defaults to sha1", default='sha1')
    parser.add_argument('-v', '--verbose', help="Verbose output, defaults to False", action='store_true', default=False)
    parser.add_argument('-t', '--threads', help="Number of threads to use, defaults to 2", default=2, type=int)
    return parser.parse_args()

def hash_file(file_path, algorithm='sha1', block_size=65536):
    """
    Hash a file using the specified algorithm
