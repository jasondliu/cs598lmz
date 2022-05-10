import mmap
import os
import re
import sys

# import common package in parent directory
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'common'))

import mongodb_client
import news_topic_modeling_service_client

from cloudAMQP_client import CloudAMQPClient

# Use your own Cloud AMQP queue
DEDUPE_NEWS_TASK_QUEUE_URL = "amqp://kxhvjxqj:4f-pC1wJ8zqG4qZ5j5m5-5W7RnXvSXzD@donkey.rmq.cloudamqp.com/kxhvjxqj"
DEDUPE_NEWS_TASK_QUEUE_NAME = "tap-news-dedupe-news-task-queue"

SLEEP_TIME_IN_SECONDS = 1

NEWS_TABLE_NAME = "news-test"

SAME_NEWS_SIMILARITY_
