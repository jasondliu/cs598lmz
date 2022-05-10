import weakref

_TIMERS = {}
_TIMER_CALLBACKS = {}
_TIMER_CALLS = {}
_TIMER_REFCOUNT = {}

_LOG = logging.getLogger("timer")
_LOG.setLevel(logging.DEBUG)

_LOG_HANDLER = logging.StreamHandler()
_LOG_HANDLER.setLevel(logging.INFO)
_LOG_HANDLER.setFormatter(logging.Formatter("%(asctime)s %(levelname)s: %(message)s"))
_LOG.addHandler(_LOG_HANDLER)

_LOG_HANDLER = logging.FileHandler("timer.log")
_LOG_HANDLER.setLevel(logging.DEBUG)
_LOG_HANDLER.setFormatter(logging.Formatter("%(asctime)s %(levelname)s: %(message)s"))
_LOG.addHandler(_LOG_HANDLER)

def _timer_callback(timer_id):
    """
    Called when the timer expires
