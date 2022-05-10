import gc, weakref
import types

from collections import defaultdict

from twisted.trial import unittest

from scrapy.utils.misc import load_object
from scrapy.utils.python import WeakKeyCache
from scrapy.utils.test import get_crawler, assert_aws_environ


class WeakKeyCacheTest(unittest.TestCase):

    def test_weakkeycache(self):
        d = WeakKeyCache(int)
        self.assertEqual(len(d), 0)
        self.assertEqual(list(d.keys()), [])
        self.assertEqual(list(d.values()), [])
        self.assertEqual(list(d.items()), [])
        self.assertEqual(list(d.keys()), [])
        self.assertRaises(KeyError, d.__getitem__, 'a')
        d['a']
        self.assertEqual(len(d), 1)
        self.assertEqual(d['a'], 0)
        d['a'] = 1
        self.assertEqual(
