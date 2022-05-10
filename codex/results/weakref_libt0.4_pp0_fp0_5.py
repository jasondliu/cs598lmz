import weakref

from . import base
from . import utils

__all__ = ['Window', 'WindowManager', 'WindowManagerMixin']


class Window(base.Container):
    """
    A window is a container that can be moved around and have a title bar.
    """

    def __init__(self, title=None, **kwargs):
        """
        :param title: The title of the window.
        """
        super(Window, self).__init__(**kwargs)
        self.title = title
        self.title_bar = base.Container(parent=self)
        self.title_bar.add_class('title')
        self.title_label = base.Label(parent=self.title_bar, text=title)
        self.title_label.add_class('label')
        self.title_label.add_class('title')
        self.title_label.add_class('title-label')
        self.title_label.add_class('window-title')
        self.content = base.Container(parent=self)
        self.content
