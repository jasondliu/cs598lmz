import threading
threading.stack_size(32768)

"""
This file defines the default configuration for the webapp.

However, we use 12-factor principals and recommend configuring using
environment variables.
"""
from os import environ, path
from tempfile import gettempdir

from boto.s3.connection import Location


try:
    # if kombu is not installed, queue settings are ignored
    BROKER_URL = environ['CELERY_BROKER_URL']
    CELERY_RESULT_BACKEND = environ['CELERY_RESULT_BACKEND']
except KeyError:
    pass

try:
    BUCKET_NAME = environ['AWS_S3_BUCKET_NAME']
except KeyError:
    BUCKET_NAME = 'starcluster'

try:
    BUCKET_LOCATION = environ.get('AWS_S3_BUCKET_LOCATION', Location.DEFAULT)
except KeyError:
    BUCKET_LOCATION = Location.DEFAULT

try:
    AWS_ACCESS_
