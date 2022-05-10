import weakref

from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _

from django_extensions.db.fields import CreationDateTimeField, ModificationDateTimeField
from django_extensions.db.models import TimeStampedModel

from django_extensions.db.fields import UUIDField


class Profile(TimeStampedModel):
    user = models.OneToOneField(User, related_name='profile')
    uuid = UUIDField()

    def __unicode__(self):
        return '%s' % self.user

    def get_absolute_url(self):
        return ('profile_detail', None, {'uuid': self.uuid})
    get_absolute_url = models.permalink(get_absolute_url)

    def save(self, *args, **kwargs):
        if not self.uuid:
            self.uuid = uuid.uuid4()
        super(Profile, self
