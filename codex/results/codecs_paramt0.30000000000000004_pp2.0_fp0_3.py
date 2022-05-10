import codecs
codecs.register_error('strict', codecs.ignore_errors)

class Command(BaseCommand):
    help = 'Import data from a CSV file'

    def add_arguments(self, parser):
        parser.add_argument('--file', type=str, help='The CSV file to import')
        parser.add_argument('--model', type=str, help='The model to import')
        parser.add_argument('--delimiter', type=str, default=',', help='The delimiter of the CSV file')
        parser.add_argument('--encoding', type=str, default='utf-8', help='The encoding of the CSV file')

    def handle(self, *args, **options):
        file_path = options['file']
        model_name = options['model']
        delimiter = options['delimiter']
        encoding = options['encoding']

        if not file_path:
            raise CommandError('You must specify the path to the CSV file')

        if not model_name:
            raise CommandError('You must specify the model to import')

        model = apps.get
