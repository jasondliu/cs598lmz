import socket

from django.conf import settings
from django.contrib.sites.models import Site
from django.core.exceptions import ImproperlyConfigured
from django.core.mail import send_mail
from django.core.management.base import BaseCommand, CommandError
from django.template.loader import render_to_string
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

from ...models import Membership, MembershipDefault


class Command(BaseCommand):
    help = _('Send membership expiry notifications.')

    def add_arguments(self, parser):
        parser.add_argument(
            '--days',
            dest='days',
            type=int,
            default=30,
            help=_('Days before expiry to send notifications.'),
        )

    def handle(self, *args, **options):
        days = options['days']
        if days < 0:
            raise CommandError(_('--days must be a positive integer.'))
        if not settings.DEFAULT_FROM_EMA
