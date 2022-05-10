from lzma import LZMADecompressor
LZMADecompressor.flush = lambda self, length: bytes()

def notify(message):
    print(message)

    if sys.platform.startswith('linux'):
        subprocess.Popen(['notify-send', message])

def add_cwd_to_sys_path():
    sys.path.insert(0, os.getcwd())

def check_dependencies():
    dependencies = '''
    requests
    urllib3
    lzma
    humanize
    flask
    flask_table
    '''
    for dependency in dependencies.split():
        try:
            __import__(dependency)
        except ImportError as e:
            print('You are missing the dependency %s' % dependency)
            sys.exit(e)

def validate_and_get_args(args):
    if len(args) < 2:
        print('Please provide url and optional: section name, password, path to config')
        sys.exit()

    url = args[1]
    name = args[2] if len(args) > 2 else None
    password
