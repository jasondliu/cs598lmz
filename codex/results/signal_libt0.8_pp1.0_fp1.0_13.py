import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

# logging
log = logging.getLogger(__name__)

# main loop
def main_loop(args, options):
  # load actions
  actions = olympus.actions.load(args)

  # setup plot
  if options.plot:
    import matplotlib.pyplot as plt
    fig = plt.figure()
    axis = fig.add_subplot(111)
    axis.grid(True)
    axis.set_xlabel('epoch')
    axis.set_ylabel('loss')
    plot_time = time.time()

  # setup state
  active_actions = []
  active_training_sets = []
  active_test_sets = []
  training_sets = []
  test_sets = []
  for action in actions:
    active_actions.append(action)
    for training_set in action.training_sets:
      training_sets.append(training_set)
      active_training_sets.append(training_
