import gc, weakref

# TODO:
#   - add support for more than one view
#   - add support for more than one controller

class View(object):
    def __init__(self, model, controller):
        self.model = model
        self.controller = controller
        self.model.add_observer(self)
        self.controller.add_observer(self)

    def update(self, observable, event):
        raise NotImplementedError

    def notify_model(self, event):
        self.model.notify_observers(event)

    def notify_controller(self, event):
        self.controller.notify_observers(event)

class Controller(object):
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.model.add_observer(self)
        self.view.add_observer(self)

    def update(self, observable, event):
        raise NotImplementedError

    def notify_model(self, event):
        self.model.
