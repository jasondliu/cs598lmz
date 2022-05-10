import codecs
codecs.register_error('ignore', codecs.ignore_errors)

from random import (seed, shuffle)
from datetime import (datetime, timedelta)
from time import (time, sleep)
from os.path import (join, exists)

from django.core.management.base import BaseCommand, CommandError

from twostream.util import (json_response)
from twostream.models import (State, Observation)


class Command(BaseCommand):
    help = 'Import saved data from disk into the database'
    args = '<directory>'

    def handle(self, *args, **options):
        if len(args) != 1:
            raise CommandError("Please specify a directory name")
        directory = args[0]

        # Set the random seed to ensure that we get the same data every time.
        # This is important because we want to be able to test the results.
        seed(0)

        # Create a list of the files in the directory.
        filenames = []
        for filename in os.listdir(directory):
            if filename.endswith(".json"
