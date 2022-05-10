import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

# These are the contants used for directory locations

IS_MAC = sys.platform == "darwin"
if IS_MAC:
    from AppKit import NSSearchPathForDirectoriesInDomains  # @UnresolvedImport
    # http://developer.apple.com/DOCUMENTATION/Cocoa/Reference/Foundation/Miscellaneous/Foundation_Functions/Reference/reference.html#//apple_ref/c/func/NSSearchPathForDirectoriesInDomains
    # NSApplicationSupportDirectory = 14
    # NSUserDomainMask = 1
    # True for expanding the tilde into a fully qualified path
    appdata = path.join(NSSearchPathForDirectoriesInDomains(14, 1, True)[0], "mpt")
else:
    appdata = path.expanduser(path.join("~", ".mpt"))

CONFIG_DIR = appdata
if not path.exists(CONFIG_DIR):
    os.mkdir(CONFIG_
