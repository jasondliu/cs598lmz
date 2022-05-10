import weakref

from pulsar.apps.test import test

from lux import forms

from . import (app, has_pyramid, has_django, has_flask, has_quart,
               has_aiohttp)


class TextForm(forms.Form):
    test_text = forms.CharField()


class TestForm(test.TestCase):
    config_file = 'tests.form'
    test_settings = {'DEBUG_SQL': 'false'}

    def test_form_meta(self):
        self.assertEqual(TextForm._meta.name, 'TextForm')
        self.assertEqual(TextForm._meta.model, 'TextForm')
