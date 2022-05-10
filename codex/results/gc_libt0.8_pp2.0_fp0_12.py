import gc, weakref

from waflib import Configure, TaskGen
from waflib.Tools import c, cxx
import waflib.Utils

from waflib.Tools.ccroot import link_task, stlink_task
from waflib.TaskGen import feature, before_method, after_method

################################################################
@feature('c', 'cxx')
@before_method('apply_link')
def apply_flags(self):
	"""
	propagate the flags provided in the flags context to the tasks created by :py:func:`waflib.Tools.ccroot.apply_link`
	"""
	flags = self.flags
	if self.env.DEST_BINFMT == 'pe':
		flags += ' ' + self.env.subst('${LINKFLAGS}')

	# extend the flags from the task generators to the link tasks
	li = getattr(self, 'link_task', None)
	if li:
		if isinstance(li, link_task):
			li.env.append_value('LINKFLAGS',
