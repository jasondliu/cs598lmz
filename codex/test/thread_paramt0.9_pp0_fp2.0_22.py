import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n')).start()
term.delay_output(5)
term.cbreak()

term.keypad(True)

try:
    sys.stdout.write('\x1b[?25h')
    sys.stdout.flush()
    for i in range(150):
        term.addstr(str(i) + ' ')
        sys.stdout.flush()
        time.sleep(0.1)
        term.move(term.getyx()[0], 0)
        term.clrtoeol()
    sys.stdout.write('\x1b[?25l')
    sys.stdout.flush()
    start = time.time()
    while time.time() - start < 5:
        pass
    sys.stdout.write('\x1b[?25h')
    sys.stdout.flush()
finally:
    term.keypad(False)
    term.norm_mode()
    term.move(25, 0)
    term.clrtoeol()
   
