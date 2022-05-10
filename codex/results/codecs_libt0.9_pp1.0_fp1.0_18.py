import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'utf8mb4' else None)

sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))

import django
django.setup()

from matches.models import Group, Match, Participant, PlayerMatchStats
from notifications.models import Notification
from users.models import Player, TeamAdmin, User
from scores.api.serializers import PlayerMatchStatsSerializer
from scores.views import send_mail_match, _get_template_match_scores, _get_template_match_scores_html, _get_template_match_scores_table
from scores.models import Score

class Command(BaseCommand):
    help = 'Notify players and admins using push notifications'

    def handle(*args, **options):
        now = datetime.datetime.now().replace(tzinfo=timezone.get_current_timezone())

        categories = [Category.IPL, Category.PRO, Category.U19
