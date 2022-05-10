import codecs
codecs.register_error('strict', codecs.ignore_errors)

import re

from django.conf import settings
from django.core.management.base import BaseCommand

from ...models import *

class Command(BaseCommand):
    args = '<filename>'
    help = 'Import a CSV file of members'

    def handle(self, *args, **options):
        if len(args) != 1:
            print "Usage: ./manage.py import_members <filename>"
            return

        f = codecs.open(args[0], encoding='utf8', errors='strict')
        reader = csv.reader(f)
        header = reader.next()

        for row in reader:
            row = dict(zip(header, row))

            try:
                member = Member.objects.get(pk=row['id'])
            except Member.DoesNotExist:
                member = Member()

            member.id = row['id']
            member.name = row['name']
            member.party = row['party']
            member.constituency = row['const
