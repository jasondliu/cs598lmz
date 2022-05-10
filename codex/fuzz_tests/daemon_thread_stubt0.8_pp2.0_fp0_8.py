import sys, threading

def run():
	global start, end, name, postfix, thread_num, cmd, mode
	if mode == 'ps':
		c = subprocess.Popen(cmd + '|grep python |grep %s |grep -v grep |wc -l' % name, shell = True, stdout = subprocess.PIPE)
		count, temp = c.communicate()
		#print count
		count = int(count)
	elif mode == 'dir':
		count = 0
		for i in xrange(start, end):
			if os.path.exists('%s%s_%d.%s' % (postfix, name, i+1, postfix)):
				count += 1
	return count

def refresh_cmd(cmd, i):
	if mode == 'ps':
		return cmd
	elif mode == 'dir':
		return '%s%s_%d.%s' % (postfix, name, i+1, postfix)

def main(thread_num,
