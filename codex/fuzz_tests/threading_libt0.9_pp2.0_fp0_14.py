import threading
threading.current_thread().name = 'MainThread'  # This is just to change the main thread name.

logger = log.Logger('Scheduler')


class Scheduler:
    def __init__(self, api_token, prod_queue, prod_lock, prod_job_count, prod_heart_beat, prod_last_submit,
                 prod_disabled, prod_job_ids, dev_queue, dev_lock, dev_job_count, dev_heart_beat, dev_last_submit,
                 dev_disabled, dev_job_ids, user, job_stop_event, job_stop_lock):
        self.api_token = api_token
        self.prod_queue = prod_queue
        self.prod_lock = prod_lock
        self.prod_job_count = prod_job_count
        self.prod_heart_beat = prod_heart_beat
        self.prod_last_submit = prod_last_submit
        self.prod_disabled = prod_disabled
        self.prod_job_ids = prod_job
