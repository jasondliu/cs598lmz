import select

from django.core.management.base import BaseCommand
from django.db import connection
from django.db.utils import OperationalError

from ...models import Event


class Command(BaseCommand):
    help = 'Wait for the database to be ready'

    def handle(self, *args, **options):
        self.stdout.write('Waiting for database...')
        db_conn = None
        while not db_conn:
            try:
                db_conn = connection.cursor()
            except OperationalError:
                self.stdout.write('Database unavailable, waiting 1 second...')
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS('Database available!'))

        self.stdout.write('Waiting for events...')
        while True:
            try:
                event = Event.objects.get(pk=1)
            except Event.DoesNotExist:
                self.stdout.write('Event unavailable, waiting 1 second...')
                time.sleep(1)
            else:
                self.
