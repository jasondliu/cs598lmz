import weakref
sub_ref = weakref.WeakValueDictionary()
sub_ref_mutex = threading.Lock()


def new_sub_ref(sub):
    global sub_ref
    global sub_ref_mutex

    with sub_ref_mutex:
        sub_ref.update({sub.subscription_id: sub})
        sub.__sub_ref_dict__ = weakref.ref(sub_ref)


class Subscription(EventEmit):
    def __init__(self, *args, **kwargs):
        super(Subscription, self).__init__()
        self.subscription_id = self.get_subscription_id()
        self.sub_list = []
        self.sub_name = 'subscription'
        new_sub_ref(self)

    def __del__(self):
        sub_ref_mutex.acquire()
        if hasattr(self, 'sub_ref_dict'):
            del self.sub_ref_dict()[self.subscription_id]
        sub_ref_mutex.release()
