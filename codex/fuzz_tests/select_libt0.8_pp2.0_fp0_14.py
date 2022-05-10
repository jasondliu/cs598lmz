import select
import sys
import time

from multiprocessing.pool import ThreadPool

from pdanalytics import settings
from pdanalytics.utils import (
    get_logger,
    get_page_stats,
    make_header,
    send_email,
)
from pdanalytics.signals import (
    initialize_rules,
    get_rules,
    get_actions,
    get_urls,
    RULES,
    ACTIONS,
    URLS,
)


@asyncio.coroutine
def fetch_url(url, session, restrict=None):
    """Return a Future object for the given URL."""
    future = asyncio.Future()
    connector = aiohttp.TCPConnector(limit=restrict)
    response = yield from session.get(url, connector=connector)
    text = yield from response.read()
    yield from response.release()
    future.set_result(text)
    return future


class Checker:
    """Check a set of URLs and alert when problems are detected"""

    def __
