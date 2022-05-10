import codecs
codecs.register_error('strict', codecs.ignore_errors)

from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from django.utils.translation import ugettext as _
from django.utils.encoding import smart_str
from django.db import transaction

from oioioi.contests.models import Contest, Submission, ProblemInstance
from oioioi.problems.models import Problem
from oioioi.programs.models import Test, OutputChecker, ModelSolution, \
        ModelProgramSubmission, ModelSolutionData, ModelProgramSubmissionData
from oioioi.programs.controllers import ProgrammingContestController
from oioioi.programs.problem_instance import ProgrammingProblemInstance
from oioioi.programs.utils import is_program_submission, is_model_solution
from oioioi.programs.package import package_test, package_model_solution
from oioioi.programs.package import package_submission, package_checker
from oioioi.programs.package import package
