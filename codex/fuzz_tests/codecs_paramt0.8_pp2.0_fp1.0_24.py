import codecs
codecs.register_error('strict', codecs.ignore_errors)

import os
import sys
import logging
import time

try:
    import curses
except ImportError:
    curses = None

# Try to import the Python Image Library (PIL)
try:
    import Image
except ImportError:
    try:
        from PIL import Image
    except ImportError:
        # This is an image rendering result, it should be safe to display
        # even if PIL isn't available
        Image = None

log = logging.getLogger("webdriver.firefox.console")


def get_gecko_log(binary, server_url, timeout=180, gecko_log_path=None):
    """Get the log from a running Gecko instance.

    This function will not return until a log line has been received from the
    Gecko process. If a Gecko process is not running, then this function will
    return immediately.

    :param binary: A Gecko binary to connect to.
    :param server_url: The URL of the WebDriver server.
    :param gecko_log_path
