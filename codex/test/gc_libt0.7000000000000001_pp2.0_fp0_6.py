import gc, weakref
import threading, queue

#import pdb

class DummyApp(object):
    """
        Dummy app for testing.
    """
    def __init__(self):
        self.data = 0

    def add_data(self):
        self.data += 1

    def show_data(self):
        print("data = {}".format(self.data))

def test_app():
    """
        Test app.
    """
    print("Testing app ...")

    app = DummyApp()
    print("App initialized")
    app.show_data()

    print("Adding data ...")
    app.add_data()
    app.show_data()

class DummyView(object):
    """
        Dummy view for testing.
    """
    def __init__(self, app):
        print("Initializing view")
        self.app = weakref.proxy(app)

    def display_data(self):
        print("Displaying data")
        print("data = {}".format(self.app.data))

