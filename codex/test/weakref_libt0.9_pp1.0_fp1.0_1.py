import weakref

class CallbackDispatcher:

    def __init__(self):
        self.callbacks = []

    def add(self, callback):
        self.callbacks.append(callback)

    def remove(self, callback):
        self.callbacks.remove(callback)

    def fire(self, *args, **kwargs):
        for callback in self.callbacks:
            callback.run(*args, **kwargs)


    def format_callbacks(self):
        names = []
        for callback in self.callbacks:
            names.append(str(callback.target_method))

        return '\n'.join(names)


class SingleMethodCallback:
    """
    A single callback, referencing a single method.
    
    The goal of this class is to enable Gio's model-view
    connect/disconnect mechanism to work with any python object
    with callback methods in it.
    """

    def __init__(self, target_method):
        """
        Create a callback.
        """
        
        # Create a weakref to the parent object,
