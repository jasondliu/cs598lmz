import sys, threading

def run():
    cwd = os.getcwd()
    sys.path.insert(0, os.path.realpath(os.path.join(cwd, '..')))
    sys.path.insert(0, os.path.realpath(os.path.join(cwd, 'analytics.zip')))
    from analytics import main
    main.main()

threading.Thread(target=run).start()
