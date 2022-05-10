import gc, weakref
from queue  import Queue
from .gtk3compat import IS_GTK3
from .util import add_pid_suffix


if IS_GTK3:
    import multiprocessing as mp
    #multiprocessing needs a real socket so we can't use a proxy
    from multiprocessing import SimpleQueue
    assert not os.environ.get("XPRA_PROXY_START_OVERRIDE")
else:
    #older versions of gtk2 don't support multiprocessing,
    #so just use a dummy module:
    mp = sys.modules.get("dummy_module")
    SimpleQueue = object


PROFILER = os.environ.get("XPRA_PROFILE_XORG")
NOTYPEMAP = os.environ.get("XPRA_NO_TYPEMAP", "0")!="0"
SESSION_MANAGER_CLIENT = os.environ.get("XPRA_SESSION_MANAGER_CLIENT")
SHADOW_SERVER = os.environ.get("XP
