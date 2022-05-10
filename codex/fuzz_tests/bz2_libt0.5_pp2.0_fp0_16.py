import bz2
bz2.BZ2File.readlines = _readlines


from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User

from optparse import make_option

from django.conf import settings
from django_fixture_magic.utils import get_model_from_string, get_fixture_file_path
from django_fixture_magic.management.commands.dumpdata import dump_data
from django_fixture_magic.management.commands.loaddata import load_data

class Command(BaseCommand):
    help = 'Create a fixture for a specific model'
    args = 'app.model'
    option_list = BaseCommand.option_list + (
        make_option('--format', default='json', dest='format',
            help='Specifies the output serialization format for fixtures.'),
        make_option('--indent', default=None, dest='indent', type='int',
            help='Specifies the indent level to use when pretty-printing output'),
        make_option('--ex
