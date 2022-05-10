import _struct
from UserString import StringIO
import StringIO

warnings.filterwarnings('ignore',category=DeprecationWarning)

# full path of this process
exepath=os.path.abspath(sys.argv[0])
# the full path of the directory which this process is in, ending with the path separator
exedir=os.path.dirname(exepath)
# the name of this process
exename=os.path.basename(exepath)
# the full path of the directory which this process's stdout and stderr will be sent to
exeoutdir=exedir


# all these remain None unless assigned below
homedir=None
bindir=None
nrgbinpath=None
configpath=None
datadir=None
stashdir=None
dbh=None

# these are derived and set up below
import update,crypto
from update import get_version
import tracing,tracerow
import conf_eng,parseopt,confset,confvalid
import geturl,inifile,log
import setupunix,
