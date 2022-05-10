import mmapi
import mm
import mmpython

def root(r):
	r.message('command', 'mm root')
	r.message('response', 'root: %s' % mm.mminfo.GetRoot())

def load(r):
	r.message('command', 'mm load')
	r.message('response', 'load: %s' % mm.mminfo.GetLoad())

def uptime(r):
	r.message('command', 'mm uptime')
	r.message('response', 'uptime: %s' % mm.mminfo.GetUptime())

def tick(r):
	r.message('command', 'mm tick')
	r.message('response', 'tick: %s' % mm.mminfo.GetTick())

def pause(r):
	paused = mm.mminfo.SetPaused(not mm.mminfo.GetPaused())
	r.message('command', 'mm pause')
	r.message('paused', '%s' % paused)

def window(r):

