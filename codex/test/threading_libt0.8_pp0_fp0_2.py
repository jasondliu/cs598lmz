import threading
threading.Event().set()
def hello(name):
    """wait for the event to be set before doing anything"""
