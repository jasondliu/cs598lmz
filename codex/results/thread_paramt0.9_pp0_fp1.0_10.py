import sys, threading
threading.Thread(target=lambda: sys.stderr.write('Hello from task2\n')).start()
 
# A new thread is started for each task.
# The time spent blocked in waits is not included in the duration.

import celery
print(celery.__version__)

# $ pip install -U Celery[redis]

# app = celery.Celery(
#     backend=celery.backends.rpc.RPCBackend(),
#     broker=celery.backends.rpc.RPCBackend()
# )
# $ pip install -U redis
# app.conf.broker_url = "redis://localhost:6379/0"
# app.conf.result_backend = "redis://localhost:6379/0"
# app.conf.update(result_expires=3600)

# app.autodiscover_tasks([__package__])

# app.conf.timezone = 'UTC'
# app.conf.beat_schedule = {
#         'add-every-30-seconds': {
#             '
