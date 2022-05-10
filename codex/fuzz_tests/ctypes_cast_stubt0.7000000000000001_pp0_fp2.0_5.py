import ctypes
ctypes.cast(0, ctypes.c_int32)
# ----------------------------------------------------------------------------

# ----------------------------------------------------------------------------
#
# ----------------------------------------------------------------------------
def ParseCommandLine():
    """Parse the command line arguments.

    Returns:
        object: options object with the arguments.
    """
    parser = argparse.ArgumentParser(
        description="""This script reads the JSON files from the
        given path and writes them to the given output file.
        """)

    parser.add_argument("--input", metavar="path", required=True,
                        help="""Path to the directory with the JSON files.""")
    parser.add_argument("--output", metavar="path", required=True,
                        help="""Path to the output file.""")

    options = parser.parse_args()

    if not os.path.isdir(options.input):
        raise ValueError("The 'input' argument is not a directory or "
                         "does not exist.")

    return options
# ----------------------------------------------------------------------------

# ----------------------------------------------------------------------------
#
# ----------------------------------------------------------------------------
def main():
    """The main function."""
    options = Parse
