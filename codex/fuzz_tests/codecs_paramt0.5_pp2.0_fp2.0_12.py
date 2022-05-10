import codecs
codecs.register_error('strict', codecs.ignore_errors)

class Test(unittest.TestCase):
    def test_form_fields(self):
        class TestForm(Form):
            name = StringField('Name')
            submit = SubmitField('Submit')

        form = TestForm()
        self.assertEqual(form.name.label.text, 'Name')
        self.assertEqual(form.submit.label.text, 'Submit')

    def test_validate_on_submit(self):
        class TestForm(Form):
            name = StringField('Name')
            submit = SubmitField('Submit')

        form = TestForm()
        self.assertFalse(form.validate_on_submit())

        form.name.data = 'test'
        self.assertFalse(form.validate_on_submit())

        form.submit.data = True
        self.assertTrue(form.validate_on_submit())

    def test_validate_on_submit_with_csrf(self):
        class TestForm(Form):
            name = StringField('Name')
