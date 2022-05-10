import codecs
codecs.register(idna_lookup)

NAME = 'Syncplay'
GIT_PATH = 'git://github.com/Syncplay/syncplay.git'
GIT_BRANCH = 'master'

def gitVersion():
    proc = Popen(['git', 'describe', '--always'], shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return proc.communicate()[0].decode('utf-8').strip()

version = '1.3.3'
build = None
if os.path.exists('.git'):
    logging.warning("Detected that we're running from a git repository, trying to get build with 'git rev-list HEAD --count'")
    build = gitVersion()

INNOSETUP_VERSION = '5.4.1'

class SyncplayBuilder(object):
    def __init__(self, innosetup_download_url=None):
        if platform.system() != 'Windows':
            logging.error("Script must be run on Windows
