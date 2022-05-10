import socket

from django.conf import settings
from django.core.management.base import BaseCommand
from django.utils.translation import ugettext_lazy as _

from oioioi.base.utils import make_html_link
from oioioi.contests.models import Contest
from oioioi.contests.utils import is_contest_admin
from oioioi.problems.models import Problem
from oioioi.programs.models import ModelSolution, Test, TestReport
from oioioi.programs.utils import get_test_kinds


class Command(BaseCommand):
    help = _("Sends an email to the admins of all problems in the contest "
             "containing information about the tests.")

    def add_arguments(self, parser):
        parser.add_argument('contest_id', nargs='?', type=str,
                            help=_("contest id"))

    def handle(self, *args, **options):
        contest_id = options['contest_id']
        if contest_id is None:

