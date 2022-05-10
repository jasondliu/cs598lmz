import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)
import gobject
gobject.threads_init()
import gtk

from kiwi.ui.delegates import Delegate
from kiwi.ui.objectlist import ObjectList, Column, AttributeColumn


class Window(Delegate):
    """Test window"""
    gladefile = 'tests.glade'


class TestModel(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return '<TestModel %s, %d>' % (self.name, self.age)


def main():
    objects = [TestModel('foo', 1),
               TestModel('bar', 2),
               TestModel('baz', 3)]

    window = Window()
    olist = window.get_widget('test')
    olist.append_column(AttributeColumn('name'))
    olist.append_column(AttributeColumn('age'))
    olist.set
