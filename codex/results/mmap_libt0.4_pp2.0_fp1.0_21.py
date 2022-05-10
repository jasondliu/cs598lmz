import mmap
import sys
import time

from pymongo import MongoClient
from bson.objectid import ObjectId

from mongo_logger import MongoLogger

class MongoLoggerTest(unittest.TestCase):

    def setUp(self):
        self.logger = MongoLogger()
        self.logger.start()

    def tearDown(self):
        self.logger.stop()

    def test_logger_writes_to_mongo(self):
        self.logger.write('test')
        self.assertEqual(self.logger.collection.count(), 1)
        self.assertEqual(self.logger.collection.find_one()['message'], 'test')

    def test_logger_writes_to_mongo_with_timestamp(self):
        self.logger.write('test')
        self.assertTrue(self.logger.collection.find_one()['timestamp'])

    def test_logger_writes_to_mongo_with_pid(self):
        self.log
