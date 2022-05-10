import codecs
codecs.register_error("strict", codecs.ignore_errors)

class Backend(object):
    """
    Base class for all backends.
    """
    def __init__(self, config):
        self._config = config
        self._logger = logging.getLogger("Backend")
        self._logger.info("Backend created")

    def __repr__(self):
        return "Backend(%s)" % self._config

    def __eq__(self, other):
        return (isinstance(other, self.__class__)
            and self._config == other._config)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash(self._config)

    def _get_config(self, key):
        try:
            return self._config[key]
        except KeyError:
            self._logger.error("Config value %s is not set.", key)
            return None

    def _get_config_bool(self, key):
        value = self
