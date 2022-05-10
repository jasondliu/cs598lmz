import codecs
codecs.register(getregentry())

lang = gettext.translation('base', 'locale', fallback=True)
lang.install()
_ = lang.gettext

#TODO:
# please don't remove the following two lines.
# it's used to notify the user to restart the gnome-shell after
# a new version of the extension has been installed.
try:
    from extension.common import areYouSureYouWantToRestartNow
    areYouSureYouWantToRestartNow()
except: pass

def log(msg):
    print "extension:", msg

# ---------------------------------------------------------------------

class GnomeShellExtension:
    """This is the main class of the extension, an instance of this class
    will be created at startup of the shell. The important methods are:
    start() and stop()
    """

    def __init__(self):
        self._install_path = os.path.dirname(__file__)+"/"
        self._data_dir = os.path.dirname(__file__)+"/data/"
        self._cache_dir =
