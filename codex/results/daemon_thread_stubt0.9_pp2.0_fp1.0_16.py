import sys, threading

def run():
    """
    Run the bot.
    """
    from csbot.bot import Bot
    from csbot.csbot import CSBot
    csbot = CSBot()
    csbot.run()
    bot = Bot(csbot, None)
    bot.run()

def main():
    import argparse
    argp = argparse.ArgumentParser(description='Run the CSBot as a daemon.')
    argp.add_argument('-f', '--foreground', help='run the process in the '
                                                 'foreground (no-daemon)',
                      action='store_true')
    argp.add_argument('-l', '--logfile', help='log messages to a file',
                      type=argparse.FileType())
    argp.add_argument('-p', '--pidfile', help='write a PID file',
                      default='csbot.pid')
    argp.add_argument('-d', '--debug', help='output debugging information',
                      action='store_true')
    args = argp.parse_args()

    if
