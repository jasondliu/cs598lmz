import weakref

from .common import *
from .view import View
from .window import Window

class Menu(View):
    def __init__(self, window=None, **kwargs):
        super(Menu, self).__init__(window, **kwargs)

        self.items = []

        self.view_size = (0, 0)
        self.view_offset = (0, 0)

        self.titles = []
        self.titles_offset = (0, 0)
        self.title_size = (0, 0)

    def set_items(self, items):
        self.items = []

        for i in items:
            self.add_item(i)

        self.layout()

    def add_item(self, item):
        i = None
        if isinstance(item, Menu):
            self.items.append((item, "menu"))
            item.parent = weakref.ref(self)
            i = item.view
        else:
            self.items.append((item, "normal"))
            i = item.view
       
