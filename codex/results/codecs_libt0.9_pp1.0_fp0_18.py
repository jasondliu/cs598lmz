import codecs
codecs.register(lambda name: name == 'cp65001' and codecs.lookup('utf-8') or None)
import sys
from models import Tweet,Trend,Tweet_Sentiment,Trend_Sentiment,Word_Sentiment,Location
from django.core.management.base import BaseCommand
from lib.Sentiment import SentimentAnalysis
from lib.Trend import TrendCalc

class Command(BaseCommand):
    # Displayed from 'manage.py help mycommand'
    help = "Add data to trends table"

    # Customise the @transaction.atomic decorator for our needs
    atomic = False

    def handle(self, *app_labels, **options):
        
        sentiment_analyser = SentimentAnalysis()
        word_sentiment = sentiment_analyser.doc_weightings()

    #    Print the tweets and sentiment scores at the
    #     moment. Just to check that the loop works
        
        trend_calcer = TrendCalc(list(Location.objects.all()))
        trend_data = trend_calcer.get_trend_data()


