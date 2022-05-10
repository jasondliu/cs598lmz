import weakref

logger = logging.getLogger(__name__)

VALID_TASKS = {
    "playbook" : playbooks.PlaybookTask,
    "tgt" : tasks.TgtTask,
    "run" : tasks.RunTask,
}

def get_host(host_name):
    host = db.api.host_query(host_name, False)
    if host is None:
        raise NotFound("Host not found: %s" % host_name)

    return host

def do_task(target, task, user=None):
    logger.debug("do task: %s" % task)
    task = json.loads(task)
    task = dict(task)

    type = task.pop("type").encode()
    if type not in VALID_TASKS:
        raise NotFound("Task type '%s' is not valid" % type)
    logger.debug("task type: %s" % type)

    if user is None:
        user = {}

    task["user"] = dict(user)

