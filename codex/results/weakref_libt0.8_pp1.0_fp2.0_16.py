import weakref
from wtforms import (Form, BooleanField, StringField, PasswordField,
                     validators)
from wtforms.validators import (ValidationError, DataRequired, Email,
                                EqualTo, Length, Regexp)
from flask_babel import lazy_gettext as _
from ..models import User


class LoginForm(Form):
    email = StringField(_('Email'), [DataRequired(), Email()])
    password = PasswordField(_('Password'), [DataRequired()])

    def validate_email(self, field):
        if not self.get_user():
            raise ValidationError(_('Invalid user'))

    def validate_password(self, field):
        user = self.get_user()

        if user is None:
            raise ValidationError(_('Invalid password'))

        if not user.check_password(self.password.data):
            raise ValidationError(_('Invalid password'))

    def get_user(self):
        return User.query.filter_by(email=self.email.data).first()


class RegistrationForm(Form):
    first
