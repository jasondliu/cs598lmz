import socket
import sys

from django.core.management.base import BaseCommand, CommandError
from django.db import transaction
from django.db.models import Q
from django.utils.translation import ugettext as _

from oioioi.base.utils import make_html_link
from oioioi.contests.models import Contest, Round
from oioioi.evalmgr.tasks import evalmgr_send_command
from oioioi.problems.models import Problem, ProblemStatement, \
        ProblemAttachment, ProblemDependency, ProblemSite, \
        ProblemPackage, ProblemSiteDependency
from oioioi.problems.package import backend_for_package, \
        ProblemPackageBackend
from oioioi.problems.utils import package_problems
from oioioi.programs.models import Test, ModelSolution, \
        OutputChecker, GroupReport, TestReport
from oioioi.zeus.models import ZeusProblemData, ZeusTest, ZeusModelSolution, \
        ZeusOutputChecker, ZeusGroupReport, ZeusTest
