import weakref
import logging
import cPickle
import time

from twisted.internet import protocol, reactor
from twisted.python import log

from zope.interface import implements

from carml import util

from carml.interfaces import IJob, IJobResult
from carml.errors import JobError, JobNotFoundError, JobTimeoutError



class Job(object):
    """
    A job that is sent to a remote host to be run.
    """
    implements(IJob)

    def __init__(self, func, *args, **kwargs):
        self.func = func
        self.args = args
        self.kwargs = kwargs


    def __repr__(self):
        return "<Job %s>" % self.func


    def run(self):
        """
        Run the function.
        """
        return self.func(*self.args, **self.kwargs)



class JobResult(object):
    """
    The result of a job.
    """
    implements(IJobResult)

