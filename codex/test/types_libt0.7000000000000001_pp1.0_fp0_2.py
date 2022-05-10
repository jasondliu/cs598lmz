import types
types.FunctionType.__name__

# noinspection PyUnresolvedReferences
def main():
    global argv, stdin, stdout, stderr
    argv, stdin, stdout, stderr = sys.argv, sys.stdin, sys.stdout, sys.stderr

    if len(argv) == 1:
        # print('Usage: jython.py <script> [<script args>]')
        return 1

    if argv[1] != '-c':
        # sys.path[0] = os.path.join(os.path.dirname(argv[0]), 'Lib')
        sys.path[0] = os.path.join(os.path.dirname(__file__), 'Lib')
        sys.path[1] = os.path.join(os.path.dirname(__file__), 'Lib', 'site-packages')
        sys.path[2] = os.path.dirname(__file__)
        sys.path[3] = os.path.dirname(argv[1])


