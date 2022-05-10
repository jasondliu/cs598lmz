import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

class BaseModel(Model):
    def __init__(self, *args, **kwargs):
        super(BaseModel, self).__init__(*args, **kwargs)
        self.create_time = int(time.time())
        self.update_time = int(time.time())

    def __getitem__(self, key):
        return getattr(self, key)

    __setitem__ = dict.__setitem__
    __delitem__ = dict.__delitem__

    def __repr__(self):
        return '<%s>' % self.__class__.__name__

    def save(self):
        self.update_time = int(time.time())
        self.put()

    def delete(self):
        self.key.delete()

    def to_dict(self):
        dict = self.to_dict()
        dict['id'] = self.key.id()
        return dict



