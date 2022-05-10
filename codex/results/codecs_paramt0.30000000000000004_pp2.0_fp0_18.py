import codecs
codecs.register_error('strict', codecs.ignore_errors)

# TODO:
# - add a way to specify the output file
# - add a way to specify the input file

class ParseError(Exception):
    def __init__(self, msg):
        self.msg = msg
    def __str__(self):
        return repr(self.msg)

def parse_file(filename):
    """Parse the file and return a list of dictionaries.

    Each dictionary has the following keys:
    - 'name': the name of the test
    - 'result': the result of the test
    - 'time': the time in seconds it took to run the test
    - 'output': the output of the test
    """
    # TODO: add a way to specify the input file
    with open(filename, 'r') as f:
        lines = f.readlines()

    tests = []
    test = {}
    for line in lines:
        if line.startswith('TEST'):
            if test:
                tests.append(test)
            test = {}
            test
