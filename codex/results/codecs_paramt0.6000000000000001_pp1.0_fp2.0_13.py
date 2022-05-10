import codecs
codecs.register_error("strict", codecs.ignore_errors)

from config import *

class Command(BaseCommand):
    def handle(self, *args, **options):
        # self.stdout.write('Starting...')
        # self.stdout.flush()

        # self.stdout.write('Getting all the files...')
        # self.stdout.flush()

        # import subprocess
        # p = subprocess.Popen(['ls', '-1', 'data'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        # out, err = p.communicate()
        # files = out.split('\n')
        files = os.listdir(DATA_DIR)

        # self.stdout.write('Creating models...')
        # self.stdout.flush()

        # for file in files:
        #     if file.endswith('.txt'):
        #         self.stdout.write('Creating model for file %s' % file)
        #         self.stdout.flush()
        #        
