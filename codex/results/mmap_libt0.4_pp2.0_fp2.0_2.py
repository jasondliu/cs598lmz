import mmap
import os
import re
import sys
import time
from datetime import datetime
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate
from subprocess import Popen, PIPE
from tempfile import mkstemp

import requests
from bs4 import BeautifulSoup
from django.conf import settings
from django.core.mail import EmailMessage
from django.core.management.base import BaseCommand
from django.utils import timezone
from django.utils.timezone import make_aware

from ...models import Attachment, Email, EmailAddress, Message, Thread


class Command(BaseCommand):
    help = "Import an mbox file"

    def add_arguments(self, parser):
        parser.add_argument("mbox", nargs="+", type=str)

    def handle(self, *args, **options):
        for mbox in options["mbox"]:
           
