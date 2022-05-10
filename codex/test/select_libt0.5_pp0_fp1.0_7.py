import select

from .. import utils
from .base import BaseHandler


class Handler(BaseHandler):
    """Polling handler for long-polling."""

    def initialize(self):
        """Initialize the handler."""
        super(Handler, self).initialize()
        self.timeout = self.settings['timeout']

    def get(self):
        """Get the long-polling connection."""
        self.write_message(
            utils.json_encode(self.get_messages()), binary=False)
        while True:
            self._wait_for_messages(self.timeout)
            if self.client_terminated:
                break
            messages = self.get_messages()
            if messages:
                self.write_message(
                    utils.json_encode(messages), binary=False)
