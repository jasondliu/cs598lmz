import gc, weakref


#
# For Log.
#
logger = logging.getLogger(__name__)


#
# For Date and Time.
#
def Localtime(t=None):
    if t is None:
        t = time.time()
    return time.localtime(t)


def Strftime(t=None):
    return time.strftime("%Y%m%d-%H%M%S", Localtime(t))


class Date(object):
    def __init__(self, t=None):
        self.date = datetime.date(*Localtime(t)[:3])

    @property
    def year(self):
        return self.date.year

    @property
    def month(self):
        return self.date.month

    @property
    def day(self):
        return self.date.day

    def __iter__(self):
        return iter(self.date.timetuple()[:3])

    def __repr__(self):
        return self.date.isoformat()


class Time(object
