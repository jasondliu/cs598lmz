import signal
# Test signal.setitimer()
#
# WNOHANG: return immediately if no child process has exited
#
# WUNTRACED: also return if a child has stopped(but not traced via ptrace)
#
# WSTOPPED: return status for traced child which has stopped
#
# WEXITED: status for child which has exited
#
# WCONTINUED: status for child which has continued after a stop
#
# WNOWAIT: don't reap, just poll status
#
# WEXITSTATUS: return exit status of the child
#
# WTERMSIG: return signal number which caused the child to stop or exit
#
# WSTOPSIG: return signal number which caused the child to stop
#
# WIFEXITED: return True if the child terminated normally
#
# WIFSIGNALED: return True if the child process terminated due to a signal
#
# WIFSTOPPED: return True if the child process is currently stopped
#
# WCOREDUMP: return True if the child produced a core dump
#
# WNOHANG: return immediately if no child process has exited

