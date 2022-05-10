import codecs
codecs.register_error('strict', codecs.ignore_errors)
codecs.register_error('ignore', codecs.ignore_errors)

class Command(BaseCommand):
    help = 'Import data from CSV file'

    def add_arguments(self, parser):
        parser.add_argument('file', nargs='+', type=argparse.FileType('r'),
                            help='CSV file to import')

    def handle(self, *args, **options):
        for input_file in options['file']:
            self.stdout.write('Importing from file: {0}'.format(input_file))
            header_row = None
            for row in csv.reader(input_file, delimiter=',', quotechar='"',
                                  error_bad_lines=False, encoding='utf-8-sig'):
                if not header_row:
                    header_row = row
                    continue
                row_dict = dict(zip(header_row, row))
                row_dict = self.clean_row(row_dict)
                row_dict = self.create
