import sys, threading

def run():
    try:
        import kodi
        kodi.loop()
        pass
    except:
        print('kodi quit')
    sys.exit(0)

def main():
    from apscheduler.schedulers.background import BackgroundScheduler
    from modules.utils import local_string as ls

    logname = datetime.now().strftime("%Y%m%d%H%M%S")
    # logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.INFO)
    logging.basicConfig(filename='log/%s.log' % logname, filemode='w',level=logging.INFO)

    # check configuration file
    logging.info('reading config file...')
    if not os.path.isfile('./configs/config.yaml'):
        logging.error('config file not found!')
        print(ls(32000))
        sys.exit(1)
    config = yaml.safe_load(open("./configs/config.yaml",
