import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'cp65001' else None)

class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):
        print("Start")
        self.stdout.write(self.style.SUCCESS('Successfully closed poll'))
        for i in range(0, 15):
            os.system("scrapy crawl %s" % (crawl_list[i]))
