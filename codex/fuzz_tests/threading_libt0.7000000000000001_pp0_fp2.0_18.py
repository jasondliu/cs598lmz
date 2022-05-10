import threading
threading._DummyThread._Thread__stop = lambda x: 42

class Command(BaseCommand):
    help = 'Starts the Celery worker'

    def add_arguments(self, parser):
        parser.add_argument('-Q', '--queues', action='append',
                            dest='queues',
                            help="The comma-separated list of queues to consume from")
        parser.add_argument('-c', '--concurrency', action='store',
                            dest='concurrency',
                            help='The number of child processes processing the queue. The default is the number of CPUs available on your system.')

    def handle(self, *args, **options):
        from celery import Celery
        from django.conf import settings
        from django.apps import apps

        queues = options['queues']
        concurrency = options['concurrency']

        worker = Celery()
        worker.config_from_object('django.conf:settings')

        if not worker.conf.result_backend:
            raise ImproperlyConfigured('A result backend is required.'
