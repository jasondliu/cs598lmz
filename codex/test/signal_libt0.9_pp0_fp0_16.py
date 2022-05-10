import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)
def guide_update(*args, **kwargs):
    global guide
    guide = Guide(pguide=kwargs["pguide"])

guides = [
    guide,
    Guide(pguide=lambda x: 2*x),
    Guide(pguide=lambda x: 0.5*x),
    Guide(pguide=lambda x: 0.5*x, naive_mean=True)
]

