import codecs
codecs.register_error('surrogate_then_replace', surrogate_then_replace)

class Command(BaseCommand):

    help = 'Import the entries in the DMOZ database'

    def handle(self, *args, **options):

        with codecs.open(args[0], encoding='utf-8', errors='surrogate_then_replace') as f:
            for line in f:
                line = line.strip()
                if line == '':
                    continue
                try:
                    title, cat_id, url = line.split('\t', 2)
                except ValueError:
                    sys.stderr.write('Error parsing line: %s\n' % line)
                    continue
                print title.encode('utf-8'), cat_id, url.encode('utf-8')
                root, cat_name = cat_id.split('/', 1)
                root_cat, created = Category.objects.get_or_create(name=root)
                if created:
                    root_cat.save()
                cat = root_cat
                for cat_name in cat_name
