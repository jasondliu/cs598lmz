import codecs
codecs.register_error('strict', codecs.ignore_errors)

class GitError(Exception):
    pass

def git(*args, **kwargs):
    #print "git", kwargs.get("cwd", "."), " ".join(args)
    gitkwargs = dict(kwargs)
    gitkwargs["stderr"] = subprocess.PIPE
    gitkwargs["stdout"] = subprocess.PIPE
    gitkwargs["stdin"] = subprocess.PIPE
    p = subprocess.Popen(["git"] + list(args), **gitkwargs)
    stdout, stderr = p.communicate()
    if p.returncode != 0:
        raise GitError(stderr.strip())
    return stdout

def git_read(*args, **kwargs):
    return git(*args, **kwargs).strip()

def git_read_lines(*args, **kwargs):
    return git_read(*args, **kwargs).splitlines()

def git_write(*args, **kwargs):
    return git
