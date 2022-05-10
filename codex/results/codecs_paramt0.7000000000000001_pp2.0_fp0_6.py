import codecs
codecs.register_error('ignore_extraneous', codecs.ignore_errors)

import re
import json

from jinja2 import Template

import zlib

import boto3

import logging
logging.getLogger('boto3').setLevel(logging.WARNING)
logging.getLogger('botocore').setLevel(logging.WARNING)

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

# Get the service resource
s3 = boto3.resource('s3')

# Get the bucket
bucket = s3.Bucket("s3://robinhood-scraper-files")

# Create an S3 client
s3 = boto3.client('s3')

# Call S3 to list current buckets
response = s3.list_buckets()

# Get a list of all bucket names from the response
buckets = [bucket['Name'] for bucket in response['Buckets']]

# Print out the bucket list
print("Bucket List: %s" % buckets)

# for
