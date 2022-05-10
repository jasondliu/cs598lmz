import codecs
codecs.register_error("strict", codecs.ignore_errors)
import csv
import os
import sys

from django.core.management.base import BaseCommand, CommandError
from django.db import transaction

from rbac.models import Role, RoleRelation
from rbac.utils import get_role_by_name, get_role_by_id
from rbac.utils import create_role, create_role_relation


class Command(BaseCommand):
    help = "Import roles (and their relations) from a CSV file."

    def add_arguments(self, parser):
        parser.add_argument("csv_file", type=str)

    @transaction.atomic
    def handle(self, *args, **options):
        try:
            with open(os.path.join(options["csv_file"]), "r") as f:
                reader = csv.reader(f)
                for row in reader:
                    self.stdout.write(
                        self.style.WARNING(
                            "Importing '%s'..." % (row[0],))
                   
