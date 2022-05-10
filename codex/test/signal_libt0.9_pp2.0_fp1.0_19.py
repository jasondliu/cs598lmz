import signal
signal.signal(signal.SIGINT, signal_handler)

opt = docopt(__doc__)

home = expanduser("~")
directory = join(home, 'cloudify-integration-tests')
tar_file_name = 'cloudify-integration-tests.tar'  # no ext
tar_file_path = join(directory, tar_file_name)

arguments = {}
if opt['-k']:
    if not opt['-u']:
        print('when specifying -k you must also specify -u')
        sys.exit(1)
    arguments['key_path'] = opt['-k']
    arguments['user'] = opt['-u']

if opt['-r']:
    arguments['repo'] = opt['-r']

if opt['-b']:
    arguments['branch'] = opt['-b']

public_download = Download(tar_file_name)
if public_download.no_local_copy(delete=True):
    public_download.download()
