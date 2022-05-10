import mmap
from os import path
import sys
from subprocess import call
from tempfile import NamedTemporaryFile
from time import time

from boto.s3.connection import S3Connection
from boto.s3.key import Key

from django.conf import settings as django_settings
from django.core.management.base import BaseCommand
from django.utils import timezone
from django.utils.encoding import smart_unicode

from aws_ses_gateway.models import AWSEmail, AWSEmailAttachment
from aws_ses_gateway.utils import get_s3_connection


class Command(BaseCommand):
    help = "Sends out emails."

    def add_arguments(self, parser):
        parser.add_argument('--processes', dest='processes', type=int, default=1,
            help='Number of processes to use for sending.')
        parser.add_argument('--chunk-size', dest='chunk_size', type=int, default=10,
            help='Number of emails to send at once.')

   
