import types
types.MethodType(lambda self: self.set_read_only(True), None, BaseModel)
types.MethodType(lambda self: self.set_read_only(False), None, BaseModel)

class AbstractBaseModel(BaseModel):
    class Meta:
        abstract = True

class BaseModelMeta(ModelBase):
    def __new__(cls, name, bases, attrs):
        new_cls = ModelBase.__new__(cls, name, bases, attrs)

        def set_read_only(self, read_only=True):
            self._read_only = read_only

        def is_read_only(self):
            return self._read_only

        def save(self, *args, **kwargs):
            if self.is_read_only():
                raise Exception("Can't save a read only instance")
            return super(new_cls, self).save(*args, **kwargs)

        setattr(new_cls, "set_read_only", set_read_only)
