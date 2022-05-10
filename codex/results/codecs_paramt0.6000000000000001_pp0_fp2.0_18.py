import codecs
codecs.register_error('strict', codecs.ignore_errors)

from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from django.utils.encoding import smart_unicode

from app import models as app_models
from app.utils import get_csv_file_path


class Command(BaseCommand):
    help = u'Импорт заявок из csv файла'

    def add_arguments(self, parser):
        parser.add_argument('--file', type=unicode, help=u'Путь к csv файлу')

    def handle(self, *args, **options):
        file_path = options.get('file')

        if file_path:
            file_path = os.path.abspath(file_path)
        else:
            file_path = get_csv_file_path()

        if not os.path.exists(file_path):
            raise CommandError(
