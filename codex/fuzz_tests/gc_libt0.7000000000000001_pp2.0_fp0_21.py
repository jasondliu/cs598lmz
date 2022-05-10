import gc, weakref

from ..utils import log
from .. import core
from ..core import settings
from ..core import filesystem
from ..core.system import system

from .. import interface
from ..interface import interface


def run(name, args, cwd=None, shell=False, detached=False, stdout=None, stderr=None, stdin=None, uid=None, gid=None, env=None, **kwargs):
	core.log.debug('running %s %s' % (name, ' '.join(args)))
	# check if the executable exists
	executable = core.system.system.which(name)

	if executable is None:
		executable = name

	# create the new process
	process = weakref.proxy(interface.Process(args, executable, cwd=cwd, shell=shell, detached=detached, stdout=stdout, stderr=stderr, stdin=stdin, uid=uid, gid=gid, env=env, **kwargs))
	
	# run the process
	return process.run()


