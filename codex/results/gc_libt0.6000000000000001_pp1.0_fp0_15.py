import gc, weakref

from django.core.exceptions import ObjectDoesNotExist
from django.test import TestCase

from django_evolution.compat import User
from django_evolution.mutations import *
from django_evolution.models import Version
from django_evolution.signature import create_project_sig, create_app_sig
from django_evolution.tests.base_test_case import EvolutionTestCase
from django_evolution.tests.models import *
from django_evolution.support import supports_index_together


class ProjectSignatureTests(TestCase):
    def test_create_project_signature(self):
        """Testing create_project_signature"""
        sig = create_project_sig()
        self.assertTrue(sig)
        self.assertTrue('tests' in sig)
        self.assertTrue('auth' in sig)

        self.assertTrue('__evolution__' in sig['tests'])
        self.assertEqual(sig['tests']['__evolution__'], [])
