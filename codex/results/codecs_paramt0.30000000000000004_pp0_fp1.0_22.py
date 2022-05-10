import codecs
codecs.register_error('strict', codecs.ignore_errors)

class Command(BaseCommand):
    help = 'Import data from old database'

    def handle(self, *args, **options):
        if len(args) < 1:
            raise CommandError('Missing argument: <old database>')

        old_db = args[0]
        if not os.path.exists(old_db):
            raise CommandError('File not found: %s' % old_db)

        self.stdout.write('Importing data from %s...\n' % old_db)
        self.import_data(old_db)
        self.stdout.write('Done.\n')

    def import_data(self, old_db):
        # Connect to old database
        conn = sqlite3.connect(old_db)

        # Import data
        self.import_users(conn)
        self.import_categories(conn)
        self.import_posts(conn)
        self.import_comments(conn)

        # Close connection
        conn.close()

    def import_
