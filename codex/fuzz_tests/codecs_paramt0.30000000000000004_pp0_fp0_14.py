import codecs
codecs.register_error('strict', codecs.ignore_errors)

# set up logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(levelname)-8s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S')

# set up command line options
parser = argparse.ArgumentParser(description='Create a new project.')
parser.add_argument('project', help='the name of the project')
parser.add_argument('-f', '--force', action='store_true', help='force overwrite of existing project')
parser.add_argument('-d', '--default', action='store_true', help='use default project layout')
parser.add_argument('-p', '--path', help='the path to the project')
parser.add_argument('--no-git', action='store_true', help='do not create a git repository')
parser.add_argument('--no-virtualenv', action='store_true', help='do not create a virtualenv')
parser
