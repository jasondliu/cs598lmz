import select


class Plugin(BasePlugin):
    """
    A listener is a plugin that listens to a specific platform.
    """
    r = redis.Redis()

    def listen(self, callback):
        """
        Loop that listens to a platform.
        """
