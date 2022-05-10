import codecs
codecs.register_error('strict', codecs.lookup_error('strict'))

import rawbotz.i18n
lang = rawbotz.i18n.language.get_language()
_ = lang.gettext

class RawbotzError(Exception):
    pass


class NoItemError(Exception):
    pass


class DuplicatedItemError(Exception):
    pass


class RawList(object):

    def __init__(self, raw_list=None):
        self.raw_list = raw_list

    def __iter__(self):
        return iter(self.raw_list)

    def get(self, item_id):
        try:
            return filter(lambda i: i.id == item_id, self.raw_list)[0]
        except IndexError:
            return None

    def exist(self, item_id):
        item = self.get(item_id)
        if item:
            return True
        return False

    def append(self, item):
        if self.exist(item.id):
            raise DuplicatedItemError()

