import select

from rq import Worker, Queue, Connection
from rq.logutils import setup_loghandlers

from redis import Redis

from app import create_app

app = create_app()

with app.app_context():
    redis_conn = Redis(app.config['REDIS_HOST'], app.config['REDIS_PORT'])
    q = Queue(connection=redis_conn)


def main():
    app.logger.info("Worker started")
    with Connection(redis_conn):
        worker = Worker(q)
        worker.work()


if __name__ == '__main__':
    main()
