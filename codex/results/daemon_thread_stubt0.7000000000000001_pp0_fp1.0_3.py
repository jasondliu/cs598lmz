import sys, threading

def run():
    return subprocess.call(["python", "-u", "./parse_graph_scores_to_csv.py"])

def run_command(command):
    pipe = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    (out, error) = pipe.communicate()
    pipe.wait()
    print(out, error)
    return out

def run_commands(commands):
    print(commands)
    return run_command("; ".join(commands))

def get_graph_scores(graph_name, score_type):
    return run_command("grep -Ri %s %s | sort | awk '{print $2, $4}'" % (graph_name, score_type))

def get_all_graph_scores(graph_name):
    return run_command("grep -Ri %s *.txt | sort | awk '{print $2, $4, $6}'" % graph_name)

def
