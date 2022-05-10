import threading
threading.settrace(stacktracer.trace_calls)


class Query(object):
    """
    Class to store a query, its (unique) id and whether it has been answered
    """
    def __init__(self, query, query_id, answered, answer=None):
        self.query = query
        self.query_id = query_id
        self.answered = answered
        self.answer = answer
        self.asked_at = datetime.datetime.now()
        

class QueryQueue(object):
    """
    Class to store the queries in a queue
    """
    def __init__(self):
        self.queue = []
        self.lock = threading.Lock()

    def add(self, query, query_id):
        """
        Adds a query to the queue
        """
        query_object = Query(query, query_id, False)
        self.lock.acquire()
        self.queue.append(query_object)
        self.lock.release()

