import socket

from django.conf import settings
from django.test import TestCase

from .utils import (
    get_redis_connection,
    get_redis_connection_from_settings,
)


class RedisUtilsTests(TestCase):

    def test_get_redis_connection_from_settings(self):
        """
        get_redis_connection_from_settings() should return a client using
        the settings.REDIS_* settings.
        """
        conn = get_redis_connection_from_settings()
        self.assertEqual(conn.connection_pool.connection_kwargs['host'], settings.REDIS_HOST)
        self.assertEqual(conn.connection_pool.connection_kwargs['port'], settings.REDIS_PORT)
        self.assertEqual(conn.connection_pool.connection_kwargs['db'], settings.REDIS_DB)
        self.assertEqual(conn.connection_pool.connection_kwargs['password'], settings.REDIS_PASSWORD)
        self.assertE
