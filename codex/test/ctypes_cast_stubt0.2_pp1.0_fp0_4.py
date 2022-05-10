import ctypes
ctypes.cast(0, ctypes.py_object)

# ___________________________________________________________________________
# Main

def main():
    """Main function."""
    parser = argparse.ArgumentParser(description='Run the test suite.')
    parser.add_argument('--verbose', '-v', action='count', default=0,
                        help='increase verbosity')
    parser.add_argument('--quiet', '-q', action='count', default=0,
                        help='decrease verbosity')
    parser.add_argument('--no-progress', '-n', action='store_true',
                        help='do not display progress bar')
    parser.add_argument('--no-capture', action='store_true',
                        help='do not capture stdout/stderr')
    parser.add_argument('--with-coverage', action='store_true',
                        help='measure code coverage')
    parser.add_argument('--cover-package', action='append', default=[],
                        help='restrict coverage to selected packages')
