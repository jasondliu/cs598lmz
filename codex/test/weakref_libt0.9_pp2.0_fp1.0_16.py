import weakref
from six import with_metaclass

from brandmeister import Brandmeister


class _APIMeta(ABCMeta):

    """
        Internal metaclass to define the custom methods,
        and add them to Brandmeister to be used by api
    """

    def __new__(cls, name, bases, attrs):
        new_class = super(_APIMeta, cls).__new__(cls, name, bases, attrs)

        for key, value in attrs.items():
            if not callable(value) or not hasattr(value, "_api_method"):
                continue

            Brandmeister.api.add(key, value)

        return new_class


class _API(with_metaclass(_APIMeta, object)):

    client = None  # brandmeister client

    def __init__(self, client):
        self.client = weakref.proxy(client)
