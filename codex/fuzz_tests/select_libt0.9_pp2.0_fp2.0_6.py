import select
import socket

import dbus


class _DbusUpstartObject(object):
    """
    The main accessor for an Upstart job object.

    :ivar str obj_id: The object path for the job object.

    :ivar str service_path: The path to the process that contains the
        Upstart job object.
    """

    def __init__(self, bus, name):
        self.bus = bus
        self.obj_id = '/com/ubuntu/Upstart/jobs/%s' % name
        self.service_path = '/com/ubuntu/Upstart'

    def _get_object(self):
        """
        Retrieve the job object.

        :rtype: dbus.ObjectProxy
        """
        return self.bus.get_object(
            self.service_path,
            self.obj_id,
        )

    def start(self, environment, wait=True):
        """
        Start up the job.

        :param dict environment: A dictionary of environment variables
            to apply while the job is running.

        :param
