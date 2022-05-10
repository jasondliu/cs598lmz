import weakref
import traceback


class Container(dict):

    def __init__(self):
        pass


class Yaml(object):

    def __init__(self):
        self._refresh()

    def _refresh(self):
        self._data = classutils.clone(yaml.load(open('config.yaml'), Loader=yaml.FullLoader))

    @property
    def _accesor(self):
        return Accessor(self._data)


class Data(object):

    def __init__(self):
        self._data = {}

    def __getstate__(self):
        return self._data

    def __setstate__(self, data):
        self._data = data

    @property
    def _accesor(self):
        return Accessor(self._data)


class AccessDict(dict):

    def __init__(self, *args, **kwargs):
        super(AccessDict, self).__init__(*args, **kwargs)
        self.__missing_exceptions = set()

    def __
