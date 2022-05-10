import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)


@click.command()
@click.option("--url", required=True, help="url of the target survey")
@click.option("--token", required=True, help="cloud system survey token")
@click.option("--poll", required=False, type=int, help="poll interval in seconds. Default: 30 seconds")
@click.option("--harvest", required=False, type=int, help="harvest window in seconds. Default: 60 seconds")
@click.option("--message", required=False, help="message to the user")
def main(url, token, poll, harvest, message):
    """Syncronization service"""
    signal.signal(signal.SIGTERM, signal_handler)
    url = url.encode("utf-8").decode("cp65001", "ignore")
    token = token.encode("utf-8").decode("cp65001", "ignore")
    poll = poll or int(os.environ.
