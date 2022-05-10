import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

import os

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'jianwen.settings')

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
