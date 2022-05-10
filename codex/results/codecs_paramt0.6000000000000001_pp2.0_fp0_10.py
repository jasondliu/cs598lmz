import codecs
codecs.register_error("strict", codecs.ignore_errors)

def extract_paths(s):
    s = s.replace("/", "\\")
    paths = []
    for p in s.splitlines():
        p = p.strip()
        if p:
            paths.append(p)
    return paths

def get_path(paths):
    if len(paths) == 0:
        return None
    return paths[0]

def get_command(cmd, *args):
    return "%s %s" % (cmd, " ".join(args))

def shell_out(cmd, *args):
    command = get_command(cmd, *args)
    print command
    return os.system(command)

def shell_out_capture(cmd, *args):
    command = get_command(cmd, *args)
    print command
    p = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    out, err = p.communicate()
   
