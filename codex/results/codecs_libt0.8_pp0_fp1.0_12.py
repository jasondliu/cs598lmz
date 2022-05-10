import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

import os
import sys

# 手动加入modules，此时会修改sys.path
sys.path.append("/home/tianyuan/tyProject/typhoon3/typhoon")

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "typhoon.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
