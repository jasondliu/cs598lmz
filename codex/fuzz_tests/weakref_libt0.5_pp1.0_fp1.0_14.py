import weakref

import pytest

from aiohttp import web
from aiohttp.web_runner import GracefulExit
from aiohttp.test_utils import make_mocked_coro, make_mocked_request


@pytest.fixture
def make_app(loop):

    def maker(*, routes=None, middlewares=None, logger=None,
              handler_args=None, access_log_class=None,
              router=web.UrlDispatcher, **kwargs):
        app = web.Application(loop=loop,
                              logger=logger,
                              handler_args=handler_args,
                              access_log_class=access_log_class,
                              router=router,
                              **kwargs)
        if routes is not None:
            app.add_routes(routes)
        if middlewares is not None:
            app.middlewares.extend(middlewares)
        return app
    return maker


def test_app_ctor(loop):
    app = web.Application(loop=loop
