import codecs
codecs.register_error('strict', codecs.ignore_errors)

class Command(BaseCommand):
    help = 'Import data from old database'

    def add_arguments(self, parser):
        parser.add_argument('--host', default='localhost')
        parser.add_argument('--user', default='root')
        parser.add_argument('--password', default='root')
        parser.add_argument('--database', default='migration')
        parser.add_argument('--port', default=3306)
        parser.add_argument('--charset', default='utf8')
        parser.add_argument('--prefix', default='')

    def handle(self, *args, **options):
        self.stdout.write('Connecting to old database...')
        old_db = MySQLdb.connect(
            host=options['host'],
            user=options['user'],
            passwd=options['password'],
            db=options['database'],
            port=int(options['port']),
            charset=options['charset']
        )
       
