import signal
signal.signal(signal.SIGINT, signal_handler)

#----------------------------------------------------------------------
def monitor(model_name, gpu_id):
    """
    Monitor the model with the given name on the curent machine
    """
    global root, controller, app, ul, ll

    if model_name:
        model = calculate_model_name(model_name, [], [])
    else:
        model = ""

    runid = os.environ.get('LSB_JOBID', "")
    jobs = getRunningJobs(runid, 1)

    app = MyApp(jobs, 1, model)
    app.mainloop()

#----------------------------------------------------------------------
if __name__ == "__main__":
    import optparse
    parser = optparse.OptionParser(usage="%prog [-g gpu_id] [model_name]")
    parser.add_option("-g", metavar="gpu_id", default=-1,
                      type="int", help="GPU ID (default: all)")
    args = parser.parse_args()[0]
