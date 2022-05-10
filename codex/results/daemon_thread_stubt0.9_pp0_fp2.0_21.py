import sys, threading

def run():
    options = dict(
        host=configuration.get('celery.host', 'localhost'),
        port=configuration.get('celery.port', 5672),
        virtual_host=configuration.get('celery.virtual_host', '/'),
    )
    for key in ['host', 'port', 'virtual_host']:
        if options[key] == '':
            del options[key]

    app = Celery('captured_events')
    app.config_from_object({
        'BROKER_URL': 'amqp://{user}:{passwd}@{host}:{port}/{virtual_host}'.format(
            user=configuration.get('celery.user', 'guest'),
            passwd=configuration.get('celery.password', 'guest'),
            **options
        ),
        'CELERY_ACCEPT_CONTENT': ['json', 'msgpack'],
        'CELERY_TASK_SERIALIZER': 'json',
        'CELERY_RESULT_SERIALIZER': '
