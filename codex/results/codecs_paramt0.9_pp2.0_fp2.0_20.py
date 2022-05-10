import codecs
codecs.register_error("strict", codecs.ignore_errors)

BROKER_URL = 'redis://localhost/0'
CELERY_RESULT_BACKEND = 'redis://localhost/0'

CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_ACCEPT_CONTENT=['json']

CELERY_ROUTES = {
    'recommend_by_id': {
        'queue': 'recommend_by_id',
        'routing_key': 'recommend_by_id'
    },
    'recommend_by_preferences': {
        'queue': 'recommend_by_preferences',
        'routing_key': 'recommend_by_preferences'
    }
}

from celery.schedules import crontab

CELERYBEAT_SCHEDULE = {
    'recommend_every_24_hours': {
        'task': 'recommend-bot.recommend_by_pre
