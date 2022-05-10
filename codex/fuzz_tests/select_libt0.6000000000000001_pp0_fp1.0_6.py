import select

from django.core.management.base import BaseCommand
from django.db import connection


class Command(BaseCommand):
    help = 'Manually run the SQL required to update the "last_seen" column'

    def handle(self, *args, **options):
        # FIXME: This is a hack to avoid running this in parallel.
        # Ideally we would get the database to do this for us.
        try:
            with open('/tmp/last_seen_lock', 'x'):
                pass
        except FileExistsError:
            print('ERROR: Another instance of this script is already running.')
            return

        # Make sure we don't hold database connections open for too long.
        old_timeout = connection.cursor().connection.get_timeout()
        connection.cursor().connection.set_timeout(60)

        try:
            self.do_work()
        finally:
            os.unlink('/tmp/last_seen_lock')
            connection.cursor().connection.set_timeout(old_timeout)

    def do_work(self):

