import sys, threading

def run():
    while True:
        sys.stdout.write("\x1b[2J\x1b[1;1H")
        p = psutil.Process(1)
        with p.oneshot() as pinfo:
            print(jinja2.Template(open('info.html').read()).render(**pinfo._asdict()), flush=True),
            for child in pinfo.children(recursive=True):
                print(jinja2.Template(open('child.html').read()).render(**child._asdict()), flush=True),
        time.sleep(1)

print(jinja2.Template(open('terminal.html').read()).render(), end='')
threading.Thread(target=run, daemon=True).start()
while True: print(input(), flush=True)
