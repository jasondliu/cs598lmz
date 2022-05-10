import socket

from django.core.management.base import BaseCommand
from django.conf import settings

from core.utils import redis_str
from core.models import Readings, Sensors


class Command(BaseCommand):
    help = "Get readings from Redis and insert them into PostGIS"

    def add_arguments(self, parser):
        parser.add_argument('--chunk-size', dest='chunk_size',
                            default=100, type=int)

    def handle(self, *args, **options):
        chunk_size = options['chunk_size']
        redis_conn = redis.StrictRedis(
            host=settings.REDIS_HOST, port=settings.REDIS_PORT)

        sensor_ids = redis_conn.smembers(settings.REDIS_SENSORS_KEY)

        for sensor_id in sensor_ids:
            while True:
                # Get readings from Redis
                readings = redis_conn.lrange(redis_str(sensor_id), 0, chunk_size)

