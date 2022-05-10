import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

def get_args():
    """
    Get command line arguments
    """
    parser = argparse.ArgumentParser(description='Create a new project')
    parser.add_argument('-p', '--project', help='Project name', required=True)
    parser.add_argument('-c', '--config', help='project config file')
    parser.add_argument('-m', '--mode', help='project mode (default: development)', default='development')
    args = parser.parse_args()
    return args

def get_config(project, config_file):
    """
    Get project config
    """
    if not config_file:
        config_file = '%s/config/%s.json' % (project, project)
    if not os.path.isfile(config_file):
        print('ERROR: Config file %s not found' % config_file)
        sys.exit(1)
    with open(config_file) as f:
        config
